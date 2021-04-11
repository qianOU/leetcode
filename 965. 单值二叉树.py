# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # bfs
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        q = [root]
        target = root.val

        while q:
            node = q.pop(0)
            if node.val != target:
                return False
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return True