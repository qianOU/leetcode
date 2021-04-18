# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(root, par):
            if root is None:
                return 

            left = dfs(root.left, root)
            right = dfs(root.right, root)

            if root.val > val:
                node = TreeNode(val)
                node.left = root
