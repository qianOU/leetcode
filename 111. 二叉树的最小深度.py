# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = [root]
        total = 0
        while q:
            total += 1
            sz = len(q)
            for _ in range(sz):
                node = q.pop(0)
                if node.left is None and node.right is None:
                    return total
                if node.left is not  None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        