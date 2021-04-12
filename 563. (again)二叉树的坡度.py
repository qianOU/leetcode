# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        total = 0
        def tranvese(root):
            nonlocal total
            if root is None:
                return 0
            
            left = tranvese(root.left)
            right = tranvese(root.right)
            total += abs(left - right)
            return left + right + root.val
        
        tranvese(root)
        return total