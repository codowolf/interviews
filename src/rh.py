from collections import defaultdict, deque
"""
Given a list of users as an array and another array which corresponds the the users they reffered, 
return a list of top 3 referrers. 
If A refers B, and B refers C, D, then A's score is 3 (since 3 users were directly or indirectly referred)
A: 3, B: 2, C: 0, D: 0

input
rh_users =  [A, B, B]
new_users = [B, C, D]
"""

def compute(rh_users, new_users):
	"""
	03/2025: RH (onsite)
	This was the code written in the interview
	"""

	graph = defaultdict(list)
	indeg = defaultdict(int)
	all_nodes = set(rh_users + new_users)

	for r, n in zip(rh_users, new_users):
		if r in graph:  # This line was changed from indeg to graph :|
			indeg[r] += 1
		else:
			indeg[r] = 1

		indeg[r] += 1
		graph[n].append(r)

	print(graph)
	print(indeg)

	start_nodes = []
	for k,v in indeg.items():
		if v == 0:
			start_nodes.append(k)

	print(start_nodes)

	deq = deque(start_nodes)
	ref_score = defaultdict(int)
	while deq:
		n = len(deq)
		for _ in range(n):
			node = deq.popleft()
			for ref in graph[node]:
				indeg[ref] -= 1
				ref_score[ref] += ref_score[node] + 1
				if indeg[ref] == 0:
					deq.append(ref)

	print(ref_score)
	return ref_score


t1 = [['x','y','z'],['y','z','k']]

#t1 = [['a', 'a', 'd', 'd', 'b', 'e', 'e', 'e'], ['c','d', 'f', 'g', 'e', 'h', 'i', 'j']]
compute(t1[0], t1[1])


