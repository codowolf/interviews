# Python

## Data Structures
- **deque**
    - is a collection-list interface
    - `append` (adds to end), `popleft` (remove from front)
- **list**
    - reverse list `[::-1]`
    - sort list based on criteria
        - `sorted(some_list, key=lamba x: x[0])`
          - sorts by first item in a list of tuples
        - `sorted(some_list, key=lambda x: -x)`
          - sorts decreasing order
        - `sorted(enumerate(some_list), key=lambda x: x[1])`
          - sorts with index next to it
- **set**
    - `add` / `remove`
    - you can also add tuples to set `myset.add((1,2))`, but not lists or any other mutable objects. Tuples are immutable
    - can do `& (union)`, `- (diff)`, `^ (symmetric diff)`
- **heapq**
    - `some_list = [(4,'bob'),(3,'ana'),(5,'eva')]`
    - NOTE: You CANNOT use key=lambda x: x[0] on heapq; it only works for sorted; The only way is to use tuples and negation. Use `-` for max heap.

| **Operation**                       | **Description**                                | **Time Complexity** |
|--------------------------------------|------------------------------------------------|---------------------|
| `heapq.heappush(heap, item)`         | Add an element to the heap                     | **O(log n)**         |
| `heapq.heappop(heap)`                | Remove and return the smallest element         | **O(log n)**         |
| `heapq.heapify(list)`                | Convert a list into a heap                     | **O(n)**             |
| `heapq.heappushpop(heap, item)`      | Push an element and pop the smallest           | **O(log n)**         |
| `heapq.nlargest(n, iterable)`        | Return the `n` largest elements                | **O(n log len(iterable))** |
| `heapq.nsmallest(n, iterable)`       | Return the `n` smallest elements               | **O(n log len(iterable))** |


- **2D array**
    - `visited = [[0] * m] * n` ❌  `visited = [[0] * n] * m` ✅
    
    - `visited = [[0] * n] * m` ❌ `visited = [[0] * n for _ in range(m)]` ✅ 

- **random**
    - `random.randint(a,b)  # a and b are inclusive`

- **strings**
    - `ord(ch) - ord('a')` can be used to track ascii values