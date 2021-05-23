# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 后序遍历
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        