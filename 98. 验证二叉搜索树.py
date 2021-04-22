# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # 二叉搜索树的验证可以使用上下界确定
        def dfs(root ,min ,max):
            
            if root is None:
                return True
            
            if min < root.val < max:
                return dfs(root.left, min, root.val) and dfs(root.right, root.val, max)

            else:
                return False
        

        return dfs(root, float('-inf'), float('inf'))