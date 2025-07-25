```
Design a highly scalable, real-time system for a **staff-level system design interview**. Focus on the core architectural components, data flow, and critical trade-offs for supporting immense concurrent user interactions and maintaining low latency under peak global load, typical of a high-volume, interactive platform.


We need to design a system for managing scheduled future transfers of Robux between players on the Roblox platform. This system also serves as a payment hold mechanism for platform payouts.

Here are the core requirements:

- Players can schedule transfers of variable Robux amounts to another player at a designated future time (from seconds to days).
- The Robux must be immediately deducted from the sender's account upon scheduling.
- Scheduled transfers must be cancellable by the sender before execution, with Robux refunded.
- The system needs to support high throughput (5,000 QPS for scheduling/cancellation) and execute payments reliably within minutes of their scheduled time (simple polling is not sufficient for short delays).
- Assume an existing Roblox payment API handles the final Robux transfer; you don't need to design that.
```


## Proposal

### Data Model
Transfers
- transfer_id
- sender_account_id
- receiver_account_id
- amount
- created_at
- transfer_at
- status: INITIATED | COMPLETED | FAILED | CANCELLED

Transactions (saga)
- root_txn_id
- parent_txn_id
- txn_id
- user_id
- txn_type: PAY | FEE | REFUND | REVERSAL
- amount
- debit_or_credit
- created_at
- transfer_id: FK
- status: SCHEDULED | COMPLETED | FAILED

TransactionSchedule
- schedule_id
- txn_id
- executed_at_or_after
- status: PENDING | QUEUED | COMPLETED
- created_at

TransferLockTable
- transfer_id
- ttl
### Approach
- transfer_service initiates transfer in initiated state
	- sync-call to transaction_service create transaction to make sure debit is completed
	- keeps transfer in INITIATED state
- transaction_service
	- follows saga pattern
	- receives transfer, creates debit row
	- creates record in schedule table
	- creates a credit row, with status SCHEDULED
	- if schedule is within one hour, then also adds to execution queue
- transaction_workers
	- loads records from schedule table every hour 
		- for PENDING status and `executed_at_or_after <= current_time`
	- adds records into ExecutionQueue for payments
	- executes payments from queue and writes new row to Transactions table
	- updates the Transfer table to completed
- execution_queue: SQS
	- can handle based on visiblity timeout
	- prioritizes "hot" payment exeuctions to be run asap
- for handling conflicting writes,
	- pessimistic lock has to be used, because optmistic lock could lead to realization after payments API
	- Any operations around actual money movement should be pessimistically locked
	- so in this case, it would be 
		- locking is needed when
			- worker is about to execute payment, and called the pay api which is suceeded but user has cancelled the payment
			- can be done by inserting a row in TransferLockTable to make sure it's not modifable
			- and after payment is done, remove it
			- but if there e xists a row in lock table, payment can't be executed

#### NOTE: The above solution, multiple LLMs call out the db polling for schedule might be bad
- need redis sorted sets but i'm skeptical
- bucketing differnt way
	- created "daily buckets" as db polling
	- for anything scheduled within the same day
		- use redis sorted sets as priority queue
		- OR use SQS with `delay seconds`
		- 