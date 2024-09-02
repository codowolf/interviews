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
[102. Binary Tree Level Order](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- use a deque
- q.append and q.popleft
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

## Level-Order "tracking" using DFS
```python
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    level_nodes = []  # keeps track of nodes at each level
    
    def level_order_dfs(root, level):
        if not root:
            return
        if level >= len(level_nodes):  # means if it's a new level
            level_nodes.append([root.val])
        else:
            level_nodes[level].append(root.val)

        level_order_dfs(root.left, level + 1)
        level_order_dfs(root.right, level + 1)

    level_order_dfs(root, 0)
    return level_nodes
``` 

[199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/description/?)
- For this problem, the right side view is do-dfs from right, and every first time entering a new level is the right most node.
The len(level_nodes) list is basically the max depth reached so far.
- Using BFS, you just have to return queue[-1] at each level


[637. Average of levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?)


