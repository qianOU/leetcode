# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.cum = 0
        # 翻序后序遍历 right root left 
        def dfs(root):
            if root is None:
                return 0
            
            right = dfs(root.right)
            self.cum += root.val
            root.val = self.cum
            dfs(root.left)

          dfs(root)
          
        return root
