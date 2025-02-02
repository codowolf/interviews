## Topological Sorting
Helps in identifying if graph has no cycles; Helps in identifying the order of valid sequence (for cases with pre-requisites)

**Steps for Topological Sort (using Kahn’s Algorithm):**
1. **Identify vertices with no incoming edges**: These are vertices that have no dependencies and can be processed first.
2. **Remove a vertex and its outgoing edges**: After processing a vertex, remove it from the graph and reduce the in-degree of its neighbors.
3. **Repeat**: Continue removing vertices with zero in-degree until all vertices are processed. If at any point no such vertex exists and the graph still has edges, this indicates the graph has cycles and cannot be topologically sorted.

**Note: you can also implement level order bfs, but it should only be done case by case. For instance, course schedule III can't be solved by level order. It's a DP problem.**
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
