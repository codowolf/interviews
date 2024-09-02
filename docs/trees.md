# Trees

**Inorder Traversal** : left → root → right

```python
def inorderTraversal(root):
    stack, result = [], []
    while stack or root:
        # Go left as far as possible, saving nodes to revisit later.
        while root:
            stack.append(root)
            root = root.left
        # Visit the last saved node and prepare to visit its right subtree.
        root = stack.pop()
        result.append(root.val)
        root = root.right
    
    return result
```
To track the path, the above doesn't help. You can do
```python
# given a tree, and a node p, find the path to p
# value of each node is unique
def dfs(root: Node, p: Node) -> list[Node]:
    stack = [root]
    visited = set()
    while stack:
        if stack[-1].val == p.val:
            break
        if stack[-1].left and stack[-1].left.val not in visited:
            stack.append(stack.left)
        elif stack[-1].right and stack[-1].right.val not in visited:
            stack.append(stack.right)
        else:
            visited.add(stack.pop().val)
    
    return stack # this has path from root to node
```


**Preorder Traversa** : root → left → right

**Postorder Traversal** : left → right → root

## Level-Order traversal / BFS
```python
def bfs(root):
    from collections import deque
    q = deque()
    q.append(root)
    while q:
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
```

In some cases you want to do dfs and also keep track of depth. 

[199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/description/?)

For this problem, the right side view is do-dfs from right, and every first time entering a new level is the right most node.
The len(level_nodes) list is basically the max depth reached so far.


Another example
[637. Average of levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?)
```python
# compute average of each level using dfs
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_avgs = []  # keeps track of averages at each depth / level

        def avgs(root, level):
            if not root:
                return 0
            
            if level >= len(level_avgs):  # this means the first time entering new level
                level_avgs.append((root.val, 1))  # saves avg,node-count
            else:
                avg, count = level_avgs[level]
                new_avg = ((avg * count) + root.val) / (count + 1)
                level_avgs[level] = (new_avg, count + 1)
            
            avgs(root.left, level + 1)
            avgs(root.right, level + 1)
        
        avgs(root, 0)
        return [k for k, v in level_avgs]

