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
   def find(self, parents: Dict[int, int], a: int):
        temp = a
        while parents[temp] != temp:
            if parents[parents[temp]] != parents[temp]:
                parents[temp] = parents[parents[temp]]
            temp = parents[temp]
        return temp
    ```
5. connected(p, q) - checks if two components are connected
6. path compression - Compressing the path while "find" by setting grandchildren as children. This ensures that at any point, the depth of tree is always a max of 2. 
7. using integers - the idea is to have unique nodes because we use dictionary to keep parents. If integers are not unique, you can quickly create a map of unique integer IDs for the object