R1 — TPS
- Design bookstore — with 100 parallel calls pseudo code
Onsite
- R1 — Tech discussion
- R2 — System Design
	- Host — VM rate limiters
- R3 — System Architecture
	- implement delete operation
		- user_table ➙ posts table ➙ likes table 
		- tables are nested
		- write multi threaded solution
		- solution
- R4 — Manager
- R5 — Coding
	- def insert(revenue: int)
		- creates a user with some id, and adds revenue associated with
		- one called once per user
		- ex: `insert(10) ➙ user_1:10`
	- def insert_v2(revenue: int, referrer: int)
		- creates a user with some id, and add revenue to the referrer
		- ex: `insert(15, 'user_1') ➙ {user_1: 25, user_2: 10}`
	- def get_k_lowest_revenues(int k, int min_revenue)
		- returns the K lowest revenue above `min_revenue` value
		- ex: `get(3, 35)` should return top 3 min revenues above 35
	- given a stream of input implement these methods

### R3
```python
def get_foreign_keys(foreign_key):
	# returns a dict of table name mapped to ids having fk
	# {'posts':[111, 222, 333], 'likes': [444, 555]}

def delete(table, item_id):
	# deletes item_id from table

def delete_all_items(table, user_id):
	deq = deque()
	deq.append((table, user_id))
	visited = set()
	visited.add((table, user_id))
	level = 0
	leveled_items[level].add((table, user_id))
	level += 1
	while deq:
		N = len(deq)
		futures = []
		related_items = []
		with ThreadPoolExecutor(max_workers=100) ex:
			for _ in range(N):
				tab, it = deq.popleft()
				futures.append(ex.submit(get_foreign_keys, it))
			for ft in as_completed(futures):
				related_items.extend(ft.result())
		
		for new_tab, new_ids in related_items.items():
			for new_id in new_ids:
				if (new_tab, new_id) not in visited:
					deq.append((new_tab, new_id))
					visited.add((new_tab, new_id))
					leveled_items[level].add((table, user_id))
		level += 1

	max_level = max(leveled_items)
	futures = []
	with ThreadPoolExecutor(max_workers=100) as ex:
		for lev in range(max_level, -1, -1):
			for item in leveled_items[max_level]:
				fut = ex.submit(delete, item[0], item[1])
				futures.append(fut)
		for ft in as_completed(fut):
			ft.result()
			# print result
	
		 
```