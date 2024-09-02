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