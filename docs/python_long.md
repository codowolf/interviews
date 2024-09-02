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