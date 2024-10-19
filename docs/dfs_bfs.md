# DFS

## Tricks
- For 2D array dfs, in some cases you may have to start DFS only from the borders. [130. Surround Regions](https://leetcode.com/problems/surrounded-regions/)


# BFS

## Double Ended BFS
- **ONLY** applicable for undirected graphs / trees (Word Ladder, Maze-solving problems)
- Same space and time complexity BUT **Practically** Faster than regular BFS
  - b: branching factor; d: depth of search
  - time & space complexity wrt to branches and depth: O(b ^ (d/2))
    - Reduces the search space from O(b^d) to O(b^(d/2)). Since BFS explores every node at a given level, the double-ended BFS reduces the depth to explore by half, making it exponentially faster.
- See dfs_bfs_long.md for more
