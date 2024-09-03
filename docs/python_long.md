# Python

- **2D array**
    - Buggy 2D array initialzation
        ```python
            def numIslands(self, grid: List[List[str]]) -> int:
                m, n = len(grid), len(grid[0])
                visited = [[0] * n] * m  # <- WRONG WAY
                visited = [[0] * n for _ in range(m)]  # <- RIGHT WAY
        ```
    - **NOTE** this is a buggy code for array initialization, because `[[0] * n] * m` will create only one row of `0`s and just copies the reference of it `m` times. Example
        ```python
        >>> visited = [[0] * 3] * 3
        >>> visited[0][0] = 1
        >>> print(visited)
         [[1, 0, 0], 
          [1, 0, 0], 
          [1, 0, 0]] 

## Sets Cheatsheet

### Basic Operations

```python
# Create an empty set
myset = set()

# Add a single element to the set
myset.add(10)   # adds the number 10 to the set

# Add multiple elements to the set
myset.update([20, 30, 40])  # adds 20, 30, and 40 to the set

# Remove an element from the set (raises KeyError if the element is not found)
myset.remove(10)  # removes the number 10 from the set

# Remove an element from the set without raising an error if the element is not found
myset.discard(20)  # removes the number 20 from the set

# Remove and return an arbitrary element from the set
element = myset.pop()  # removes and returns an arbitrary element from the set

# Clear all elements from the set
myset.clear()  # removes all elements from the set
```

### Set Operations
```python
# Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # {1, 2, 3, 4, 5}

# Intersection of two sets
intersection_set = set1 & set2  # {3}

# Difference of two sets
difference_set = set1 - set2  # {1, 2}

# Symmetric difference of two sets
sym_diff_set = set1 ^ set2  # {1, 2, 4, 5}

# COMPARISON Operations

# Check if a set is a subset of another set
is_subset = set1 <= set2  # True if set1 is a subset of set2

# Check if a set is a superset of another set
is_superset = set1 >= set2  # True if set1 is a superset of set2

```
### Set Notes 
- Hashable Elements (Allowed)
    - Numbers: int, float, complex
    - Strings: "hello", "world"
    - **Tuples: (1, 2, 3) (All elements inside must be immutable)**
        - this is specifically useful for tracking matrix index
    - Booleans: True, False
    - Frozen Sets: frozenset([1, 2, 3])
- Non-Hashable Elements (Not Allowed) (raises Error)
    - Lists: [1, 2, 3]
    - Dictionaries: {'a': 1, 'b': 2}
    - Sets: {1, 2, 3}