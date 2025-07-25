
# BFS

## Simple vs Level BFS

### Simple BFS
```python
while q:
	node = q.popleft()
	for neighbor in node.neighbors():
		# some processing
return
```
All nodes are processed **exactly** like level order BFS, **including level by level**, but there's no way to know when the level marking is done, so we can't compute distance by level.
### Level Order BFS
> [!tip] LevelOrder BFS — Used when after each level, there needs some counting to be done
```python
while q:
	N = len(q)
	for _ in range(N):
		node = q.popleft()
		for neighbor in node.neighbors():
			# some processing
	distance += 1
```
Note that above code has to compute **distance**, so level order is certainly needed here


## Double Ended BFS
### Summary of Comparison (with Practical Considerations and Branching Factor)


| **Algorithm**        | **Time Complexity**   | **Space Complexity** | **Practical Considerations**                                                                                                                                                                                                                                                       |
| -------------------- | --------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Normal BFS**       | O(V + E) / O(b^d)     | O(V)                 | - Explores the entire graph from one end.<br>- Can be inefficient when the target is far from the source.<br>- **Branching**: Searches all nodes up to depth **d**, leading to **O(b^d)** complexity, where **b** is the branching factor.                                         |
| **Double-Ended BFS** | O(V + E) / O(b^(d/2)) | O(V) (2x memory)     | - Reduces the search space by exploring from both ends.<br>- **Branching**: Effectively cuts depth in half, leading to **O(b^(d/2))** complexity.<br>- Requires two queues and two visited sets.<br>- In practice, explores far fewer nodes, especially in large or sparse graphs. |

---

### Key Takeaways:
- **Normal BFS** explores the entire search tree of depth **d**, making it **O(b^d)** in terms of the branching factor.
- **Double-Ended BFS**, by starting from both ends, reduces the search depth to **d/2**, effectively cutting down the number of nodes to explore to **O(b^(d/2))**. This can provide an exponential improvement in practice, especially in scenarios with a high branching factor **b**.

---

### Code 
```python
def bidirectional_bfs(graph, start, end):
    if start == end:
        return 0
    
    queue_start, queue_end = deque([start]), deque([end])
    visited_start = {start: 0}  # could be just a set if no need to track distance measurement
    visited_end = {end: 0}
    
    while queue_start and queue_end:
        # Expand from the start side; this also ensures balanced approach
        if len(queue_start) <= len(queue_end):
            result = expand(queue_start, visited_start, visited_end, graph)
        else:
            result = expand(queue_end, visited_end, visited_start, graph)
        
        if result:
            return result
    
    return -1  # No path found

def expand(queue, visited_current, visited_other, graph):  # this is like a level-step function
    current_node = queue.popleft()
    
    for neighbor in graph[current_node]:
        if neighbor in visited_other:
            # Found connection between start and end searches
            return visited_current[current_node] + visited_other[neighbor] + 1
        
        if neighbor not in visited_current:
            visited_current[neighbor] = visited_current[current_node] + 1
            queue.append(neighbor)
    
    return None
```

Examples
1. [Word Ladder](https://leetcode.com/problems/word-ladder/)


### BFS With Path Tracing

#### Single Min Path
Great question! When you use **BFS (Breadth-First Search)** to find a path from a source to a destination in a graph, the easiest and most common way to **trace the path** is to use a **parent (or predecessor) map**. Here’s how you can do it:

**1. During BFS, store the parent of each node**
- When you visit a new node `v` from node `u`, record that `u` is the parent of `v`.
- This is usually done with a dictionary or array: `parent[v] = u`.

**2. After reaching the destination, reconstruct the path**
- Start from the destination node and repeatedly look up its parent, building the path in reverse.
- Stop when you reach the source node.

**3. Reverse the path to get it from source to destination**

```python
from collections import deque

def bfs_path(graph, source, destination):
    queue = deque([source])
    visited = set([source])
    parent = {source: None}

    while queue:
        current = queue.popleft()
        if current == destination:
            break
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # Reconstruct path
    path = []
    node = destination
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()
    
    # If the source is not at the start, no path was found
    if path[0] != source:
        return None
    return path

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(bfs_path(graph, 'A', 'F'))  # Output: ['A', 'C', 'F']
```

#### Multiple Shortest Paths
Great follow-up! If you want to **print all possible shortest paths** from source to destination using BFS, you need to:

1. **Find the shortest path length** using BFS.
2. **Backtrack all possible paths** of that length from destination to source.

This is a classic problem. The key is to:
- During BFS, **record all possible parents** for each node (not just one)
```python 
elif visited[neighbor] == visited[current] + 1: # if nbh already visited, then see if it's shortest
	parents[neighbor].append(current)
```

- After BFS, **use backtracking (DFS or recursion)** to enumerate all paths from destination to source using the parent map.
```python
from collections import deque, defaultdict

def all_shortest_paths(graph, source, destination):
    # Step 1: BFS to find shortest path length and record all parents
    queue = deque([source])
    visited = {source: 0}  # node: distance from source
    parents = defaultdict(list)  # node: list of parents

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited[neighbor] = visited[current] + 1
                parents[neighbor].append(current)
                queue.append(neighbor)
            elif visited[neighbor] == visited[current] + 1:
                parents[neighbor].append(current)

    # If destination not reached
    if destination not in visited:
        return []

    # Step 2: Backtrack all paths from destination to source
    results = []
    path = [destination]

    def backtrack(node):
        if node == source:
            results.append(path[::-1])
            return
        for parent in parents[node]:
            path.append(parent)
            backtrack(parent)
            path.pop()

    backtrack(destination)
    return results

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
paths = all_shortest_paths(graph, 'A', 'F')
for p in paths:
    print(p)
```

**Output:**
```
['A', 'C', 'F']
['A', 'B', 'E', 'F']
```

# DFS
## Classic
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    self.dfs(grid, i, j, visited)
                    count += 1
        return count
    
    def dfs(self, gr, x, y, visited):
        if (x < 0) 
	        or (y < 0) 
	        or (x >= len(gr)) 
	        or (y >= len(gr[0])) 
	        or (visited[x][y]) 
	        or (gr[x][y] == '0'):
            return
        visited[x][y] = 1
        self.dfs(gr, x + 1, y, visited)
        self.dfs(gr, x, y + 1, visited)
        self.dfs(gr, x - 1, y, visited)
        self.dfs(gr, x, y - 1, visited)
```

