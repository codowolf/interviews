# Important Tips
## BFS Bulk(pruning) vs Individual
- Apply BFS at the same time
	- Problems like shortest path to **all gates from all empty points**
		- https://leetcode.com/problems/walls-and-gates/description/ 
		- Option 1 — apply BFS from gates
			- put ALL gates in DEQ and apply BFS
			- This case, when an empty cell is visited first time, it's already shortest path to it. It doesn't have to be explored by other gates
			- Meaning, **each cell is visited ONLY once** — This is pruning
		- Option 2 — apply BFS individually from gates
			- In this case, each BFS has to visited all cells as there is no way to prune
	- Another example — [01 Matrix](https://leetcode.com/problems/01-matrix/description/)
- Apply BFS individually 
	- For problems where we would have to count a visit from each node, then there has to be BFS from each node.
	- [Shortest Distance from all buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/description/) Here we need to compute distance from **ALL** buildings to the specific land, i.e, you have to know the distance to each cell, from each spot. 

## Recursive DFS vs Topology BFS
- If a DAG is given as edges, the solutions depend on how you build the graph
	- DFS helps to backtrack counts back to the parent node
		- Referral count — basically the root node will have higher count
	- Topology avoids backtrack and computes at every step
		- Server load 
		- Keeping track of indegree becomes important
		- Use topology only if DFS can't be used (mostly DAG cycle problems)
## Topological Sorting
Helps in identifying if graph has no cycles; Helps in identifying the order of valid sequence (for cases with pre-requisites)

**Steps for Topological Sort (using Kahn’s Algorithm):**
1. **Identify vertices with no incoming edges**: These are vertices that have no dependencies and can be processed first.
2. **Remove a vertex and its outgoing edges**: After processing a vertex, remove it from the graph and reduce the in-degree of its neighbors.
3. **Repeat**: Continue removing vertices with zero in-degree until all vertices are processed. If at any point no such vertex exists and the graph still has edges, this indicates the graph has cycles and cannot be topologically sorted.

 > [!tip] Note: you can also implement level order bfs, but it should only be done case by case. For instance, course schedule III can't be solved by level order. It's a DP problem.

```python
"""
You need 3 data structures
1. an adjacency list for the graph
2. an indegree map for vertices
3. a simple queue to kinda-"bfs" on indegree 0 vertices
"""
# Given vertices numbered 0-n, and directed-edges, check if graph has no cycle
# (this basically translates to can you finish all course?)
def has_no_cycle(n: int, edges: List[List[int]]) -> bool:
    indegree = [0] * n  # init indegree of all vertices to 0
    graph = defaultdict(list)
    for a,b in p:
        # directed edge (b -> a)
        indegree[a] += 1  # increment indegree
        graph[b].append(a)

    q = [e for e in range(n) if not indegree[e]]  # collect all 0 indegree vertices
    while q:
        neighbors = graph[q.pop()]  # reduce indegree for each neighbors
        for e in neighbors:
            indegree[e] -= 1
            if indegree[e] == 0:  
                q.append(e)
            # an indegree of a cycle can never be zero, so the while loop never goes into infinite loop

    return not any(indegree)
```
[204. Course Schedule](https://leetcode.com/problems/course-schedule/description/)

## Minimal Spanning Tree
- Undirected graph
- Connecting all the nodes such that the cost in minimal 
- Helps find min cost to connect all nodes
- **DOES NOT** mean shortest distance between two nodes
- Only means sum of all edge weights are minimum
- Is not unique. There could be multiple selection of edges that lead to minimal
- Only applies to connected graph. For disconnected, it leads to multiple graphs (forest) 
### Krsukal's MST
- Sort all edges
- For each edge, check if nodes are connected. (Union Find)
- The idea is, for already connected nodes, we want to avoid loops
- If not connected, connect them
- when all edges are processed, or all nodes are connected, you're done.

# Shortest Path Algos

## Dijkstra's (positive edges ONLY)
- watch this video — https://www.youtube.com/watch?v=CerlT7tTZfY 
- BFS, but with **priority queue** instead of normal queue
- 
```python
pq = []
init_distance = 0
pq.append((init_distance, start_node))

visited = set()
min_distances = {node: inf for node in all_nodes}
min_distances[start_node] = 0
while pq:
	distance_to_cur_node, cur_node = heapq.heappop(pq)
	if cur_node in visited:
		continue
	visited.add(cur_node)  # after pop, instead of after add
	for neighbor, distance_to_neighbor in cur_node.neighbors():
		total_distance = distance_to_cur_node + distance_to_neighbor
		if total_distance < min_distances[neighbor]:
			min_distances[neighbor] = total_distance
			heapq.heappush(pq, (total_distance, neighbor))	
		
```

> [!tip] Note that we add to visited **after pop** instead of **after add**, and this may result in same node added to PQ more than once, but since it's a PQ, the one with shortest distance to it will be popped first, ie explored first. `ex: PQ=[(2, 'node_A'), (3, 'node_B'), (6, 'node_B')]` Here, node_B was reached twice from two paths, at a distance of 3 and 6

## Bellman-Ford (works for negative edges as well)
