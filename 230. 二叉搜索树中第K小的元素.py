# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def traverse(root):
            if root is None:
                return 
            
            yield from traverse(root.left)
            yield root.val
            yield from traverse(root.right)
        
        iterator = traverse(root)
        for _ in range(k):
            ans = next(iterator)
        return ans