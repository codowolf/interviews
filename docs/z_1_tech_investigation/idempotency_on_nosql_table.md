# Handling Idempotency



## Actual Solution
### Storing ID mapping
Imagine stripe — when you create a transaction, they create a mapping and return success. If you try to create it again, they will return the status of the transaction. They will generate a transaction ID on their side and give it to you. The concept is essentially the same.

```python
IdempotencyTable
	hash_key=client_transaction_id
	txn_id=generate_random_id()

TransactionTable:
	hash_key=idempotency_table.txn_id
	client_id=idempotency_table.client_transaction_id
```

Any number of attempts to create a transaction will only happen once
```python
def create_transaction(client_transaction_id):
	# Both operations are consistent read or write
	idemp_record = IdempotencyTable.get_or_create(client_transaction_id)
	transaction = TransactionTable.get_or_create(idemp_record.txn_id)
	return transaction.txn_id
```


## Initial Prompting
Let me describe a problem with Dynamodb I have. 

I have some data from 3rd party, lets call it "feature", so I need to store features in ddb. 

Each feature is unique, and 3rd party  provides a unique ID. 

I need to make sure the "creation" of feature is idempotent. So I can model as
FeaturesTable
Feature — (hash_key=client_feature_id)

This ensure that there's no way I can create two records of same feature. 

Problem is that it's an anti-pattern. A row should have PK to be system generated ID. Is this right? 

If so, I could do something like this
```
Feature:
	hash_key=generate_system_id
	GSI=client_feature_id
```

However, checking GSI before writing is not right, because GSI is eventual consistent. Even if not, check on write can always lead to two writes. In this case, two records with same feature ID could be written. 

The last option is to have a separate Idempotency table, along with Features table
```
IdempotencyRecord:
	hash_key=client_feature_id
```

The code would look something like this
```python
if create_idemp_record(client_feature_id):
  create_feature_record(generate_system_id)
```

This ensures that only one call can create idemp_record. 
The second fall will fail because record is already present. But should it retry? Lets see about that. 

In the above code, the call after creating idemp record could fail, leaving the system in bad state — without creating a feature. SO YES, there should be some retry.

We could do the below to handle RETRY, but it's the same problem. GSI is eventual consistent and that's exactly we want to avoid — check and write
```python
if create_idemp_record(client_feature_id):
  create_feature_record(hash_key=generate_system_id(), GSI=client_feature_id)
else:
	if has_feature_record(GSI=client_feature_id):
		create_feature_record(hash_key=generate_system_id(), GSI=client_feature_id)
```


The other option to handle this would be to add a TTL to idemp record
```
IdempotencyRecord:
	hash_key=client_feature_id
	dynamo_expiration_time_sec=current_time + 10seconds
```

So the below code would be enough for retires
```
if create_idemp_record(client_feature_id):
	if has_feature_record(gsi=client_feature_id):
		return
	create_feature_record(generate_system_id)
else:
	raise RetryableError('Row locked, retry in 10s')
```

This would ensure that RETRY attempts will still go through, but only after 10 seconds, which would have enough time for GSI to have the replication done and `hash_feature_record` will successfully retrieve it. 

But that's a big assumption about eventual consistency. What if it's not present even after 10 seconds? How is this problem generally solved? I know you would say, we could use DDB's TransactionWrite, but lets assume we have old libraries that doesn't support TransactionWrites yet. If it was a SQL table, it could have been solved with atomic writes.