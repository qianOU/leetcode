# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(root, records):
            if root is None:
                return  -1
            
            l_d = dfs(root.left, records)
            r_d = dfs(root.right, records)
            records =  
