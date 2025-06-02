# BFS

## Simple vs Level BFS

#### Simple BFS
```python
while q:
	node = q.popleft()
	for neighbor in node.neighbors():
		# some processing
return
```
All nodes are processed **exactly** like level order BFS, **including level by level**, but there's no way to know when the level marking is done, so we can't compute distance by level.
#### Level Order BFS
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