# Python

## Data Structures
- **deque**
    - is a collection-list interface
    - `append` (adds to end), `popleft` (remove from front)
- **list**
    - reverse list `[::-1]`
    - sort list based on criteria
        - `sorted(some_list, key=lamba x: x[0])` (sorts by first item in a list of tuples)
        - `sorted(some_list, key=lambda x: -x)` (sorts decreasing order)
- **set**
    - `add` / `remove`
- **heapq**
    - `heapify(some_list, key=lambda x: x[0])`

- **2D array**
    - `visited = [[0] * m] * n` ❌  `visited = [[0] * n] * m` ✅
    
    - `visited = [[0] * n] * m` ❌ `visited = [[0] * n for _ in range(m)]` ✅ 
        
        