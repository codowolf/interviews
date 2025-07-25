https://www.hellointerview.com/learn/system-design/patterns/dealing-with-contention 

> [!tip] Contention Tip: 
> **The best candidates identify contention problems before they're asked. When designing any system with shared resources, immediately address coordination**
>
> *"This auction system will have multiple bidders competing for items, so I'll use optimistic concurrency control with the current high bid as my version check."*
>  
>  *"For the ticketing system, I want to avoid users losing seats after filling out payment info, so I'll implement seat reservations with a 10-minute timeout."*
>  
>  *"Since we're sharding user accounts across databases, transfers between different shards will need distributed transactions. I'll use the saga pattern for resilience."*
#### Using Redis TTL
```bash
SET lock:ticket:123 "locker_thread_id_123" NX PX current_time + 30
```
- SET sets the KEY-VALUE
- NX "not exists" — Only set if does not exist `if it does, then errors`
- PX — xPiration time

| key             | value                | TTL                |
| --------------- | -------------------- | ------------------ |
| lock:ticket:123 | locker_thread_id_123 | current_time + 30s |
| lock:ticket:456 | locker_thread_id_456 | current_time + 30s |
|                 |                      |                    |
#### Using DDB TTL
- same as above 
#### Using SQL table without TTL
- If TTL is not enabled, then callers can use `expire_after` to check expiry
- But to avoid clock skew, use the same time source for time — db timestamp
```python
lock = Lock.get('lock:ticket:123')
if lock:
	current_db_ts = DB.CURRENT_TIMESTAMP
	if lock.locked_at + lock.expire_after < current_db_ts:
		# it is expired
		lock.value = 'locker_thread:222'
		lock.locked_at = current_db_ts
		lock.expire_after = 30
		prev_version = lock.version
		lock.version = lock.version + 1
		lock.save(condition=f'version:{prev_version}')
```

| key             | value             | locked_at | expire_after | version_id |
| --------------- | ----------------- | --------- | ------------ | ---------- |
| lock:ticket:123 | locker_thread:123 | 1000      | 30           | 1          |
| lock:ticket:456 | locker_thread:456 | 2000      | 15           | 1          |
#### Using DDB / SQL table without TTL but with separate TTL endpoint (NOT PREFERRED)
- Since DDB doesn't provide db timestamp, it's not possible to avoid clock skew just by using external timestamps
- We can still use same data model, but a recovery endpoint to expire the item

```python
locker_id = get_thread_id()
current_time = time.utcnow()
ttl_payload = {'locker_id': locker_id, 'expire_after': current_time + 30}
enqueue_for_TTL(recovery_payload)  # this will be executed after x seconds
acquire_lock = Lock.create('lock:ticket:123', locker_id)
```

- This not preferred as it's possible that DELETION could be delayed depending on how TTL processing gets executed. It should be fast and on time![[resource_contention1.png]]

![[resource_contenttion2.png]]
![[resource_contention3.png]]