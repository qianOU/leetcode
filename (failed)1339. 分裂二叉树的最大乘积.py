# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        self.max = -1
        # 后序遍历
        def dfs(root):
            if root is None:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)

            if 