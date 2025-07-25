## Notes
1. Union Find is used in Kruskal's Minimal Spanning Tree Algorithm
2. All nodes have to be initialized by adding to map and pointing to itself.
    ```python
    for e in range(n):
        parents[e] = e
    ```
3. union(p, q) - merge subset containing p and q
    ```python
    def union(self, parents, a, b):
        pA = self.find(parents, a)
        pB = self.find(parents, b)

        if pA != pB:
            parents[pB] = pA
        return
    ```
4. find(p) - find subset element that has p
```python
# PATH HALVING (not full compression)
def find(self, parents: Dict[int, int], a: int):
	temp = a
	while parents[temp] != temp:
		if parents[parents[temp]] != parents[temp]:
			parents[temp] = parents[parents[temp]]
		temp = parents[temp]
	return temp

# FULL PATH COMPRESSION
def find(self, a):
    if self.parents[a] != a:
        self.parents[a] = self.find(self.parents[a])
    return self.parents[a]

```

5. connected(p, q) - checks if two components are connected
6. path compression - Compressing the path while "find" by setting grandchildren as children. 
7. This doesn't necessarily mean that depth is a fixed size. Because, when union happens on two root nodes, the path compression doesn't kick in.
8. If union of roots keep happening, then max depth can be number of unions (until all nodes are connected) into a single component
9. using integers - the idea is to have unique nodes because we use dictionary to keep parents. If integers are not unique, you can quickly create a map of unique integer IDs for the object


## More on full path compression
Let me show you the difference between your **path halving** and full **path compression** with a concrete example.

First, let's set up a chain structure:

```python
# Initial setup: 0 -> 1 -> 2 -> 3 -> 4 -> 5
uf = UnionFind(6)
uf.parents = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 5}
```

### Your Path Halving Implementation

When you call `find(0)`:

```python
# Step 1: temp = 0
# parents[0] = 1, parents[1] = 2
# Update: parents[0] = 2 (skip over 1)
# Move: temp = 2

# Step 2: temp = 2  
# parents[2] = 3, parents[3] = 4
# Update: parents[2] = 4 (skip over 3)
# Move: temp = 4

# Step 3: temp = 4
# parents[4] = 5, parents[5] = 5
# No update (grandparent == parent)
# Move: temp = 5

# Result after find(0):
# 0 -> 2 -> 4 -> 5
# 1 -> 2
# 3 -> 4
```

### Full Path Compression

```python
def find_with_compression(self, a):
    if self.parents[a] != a:
        self.parents[a] = self.find_with_compression(self.parents[a])
    return self.parents[a]
```

When you call `find_with_compression(0)`:

```python
# Recursively finds root = 5
# Then on the way back, updates ALL nodes to point to 5

# Result after find(0):
# 0 -> 5
# 1 -> 5  
# 2 -> 5
# 3 -> 5
# 4 -> 5
# 5 -> 5
```

## Visual Comparison

**Before find(0):**
```
0 -> 1 -> 2 -> 3 -> 4 -> 5
```

**After find(0) with your path halving:**
```
0 -----> 2 -----> 4 -> 5
     1 ↗      3 ↗
```

**After find(0) with full path compression:**
```
0 -> 5
1 -> 5
2 -> 5
3 -> 5
4 -> 5
```

## Performance Impact

- **Path halving**: Reduces path length by ~half each time
- **Path compression**: Makes all nodes point directly to root

For subsequent `find(0)` calls:
- Your version: Still needs 3 hops (0 -> 2 -> 4 -> 5)
- Full compression: Only 1 hop (0 -> 5)

Path halving is simpler to implement iteratively but slightly less efficient than full path compression. Both achieve similar amortized complexity in practice, though full compression is theoretically better.