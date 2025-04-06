
#### Rounds
- Coding Round
	- Dashmart below
- Project Deepdive
	- Too much stress on what was the actual problem, metrics of the problem
		- It seemed like he was thinking we didn't do enough research on the problem before jumping to solutions

#### Coding Round
```python
A DashMart is a warehouse run by DoorDash that houses items found in convenience stores, grocery stores, and restaurants. We have a city with open roads, blocked-off roads, and DashMarts.

City planners want you to identify how far a location is from its closest DashMart.

You can only travel over open roads (up, down, left, right). Locations are given in `[row, col]` format.

Example 1:

Given a grid where:
- 'O' represents an open road that you can travel over in any direction (up, down, left, or right).
- 'X' represents a blocked road that you cannot travel through.
- 'D' represents a DashMart.

The grid is provided as a 2D array, and a list of locations is provided where each location is a pair `[row, col]`.
[
  ['X', 'O', 'O', 'D', 'O', 'O', 'X', 'O', 'X'], #0
  ['X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X'], #1
  ['O', 'O', 'O', 'D', 'X', 'X', 'O', 'X', 'O'], #2
  ['O', 'O', 'D', 'O', 'D', 'O', 'O', 'O', 'X'], #3
  ['O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X'], #4
  ['X', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'X'], #5
]

List of pairs `[row, col]` for locations:
[
  [200, 200],
  [1, 4],
  [0, 3],
  [5, 8],
  [1, 8],
  [5, 5],
]

Your task is to return the distance for each location from the closest DashMart.

Provided:

- `city: char[][]`
- `locations: int[][]`

**Return:**

- `answer: int[]`

def get_distance_grid(city, deq, distance_grid):
  m, n = len(city), len(city[0])
  while deq:
    N = len(deq)

    for _ in range(N):
      ci, cj, prev_distance = deq.popleft()

      for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nci, ncj = ci + di, cj + dj

        if nci >= 0 and nci < m and ncj >= 0 and ncj < n:
          if city[nci][ncj] == 'O' and distance_grid[nci][ncj] == -1:
            distance_grid[nci][ncj] = prev_distance + 1
            deq.append((nci, ncj, prev_distance + 1))
          elif city[nci][ncj] == 'X' and distance_grid[nci][ncj] == -1:
            # requirement is that we still want to know distance from
            # 'X' nodes but we cannot continue from there
            distance_grid[nci][ncj] = prev_distance + 1

  return distance_grid

def compute_distances(city, locations):
  m, n = len(city), len(city[0])
  distance_grid = [[-1] * n for _ in range(m)]
  from collections import deque
  deq = deque()
  for i in range(m):
    for j in range(n):
      if city[i][j] == 'D':
        distance_grid[i][j] = 0
        deq.append((i, j, 0))

  distance_grid = get_distance_grid(city, deq, distance_grid)
  for e in distance_grid:
    print(e)

  res = []
  for location in locations:
    x, y = location
    if x >= 0 and x < m and y >= 0 and y < n:
      res.append(distance_grid[x][y])
    else:
      res.append(-1)

  return res


city = [
  ['X', 'O', 'O', 'D', 'O', 'O', 'X', 'O', 'X'], #0
  ['X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X'], #1
  ['O', 'O', 'O', 'D', 'X', 'X', 'O', 'X', 'O'], #2
  ['O', 'O', 'D', 'O', 'D', 'O', 'O', 'O', 'X'], #3
  ['O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X'], #4
  ['X', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'X'], #5
]



def test1():
  locations = [
  [200, 200],
  [1, 4],
  [0, 3],
  [5, 8],
  [1, 8],
  [5, 5],
]
  print(compute_distances(city, locations))

test1()

```
