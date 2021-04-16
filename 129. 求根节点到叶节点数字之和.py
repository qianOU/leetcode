# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # 前序遍历
        self.ans = 0
        def dfs(root, cum):
            if root is None:
                return 0
            
            cum = cum*10+root.val 
            if root.left is None and root.right is None:
                self.ans += cum
            
            
            dfs(root.left, cum)
            dfs(root.right, cum)
        
        dfs(root, 0)
        return self.ans