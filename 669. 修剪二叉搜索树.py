# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        
        # 前序
        def dfs(root):
            if root is None:
                return
            if root.val < low:
                # 注意不能直接返回 root.right, 要对root.right 也进行范围判断
                # return root.right
                return dfs(root.right)
            if root.val > high:
                # return root.left
                return dfs(root.left)
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            return root
        
        return dfs(root)
            
