# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if root is None:
            return              

        self.max_d = -1
        self.node = root.val
        
        def dfs(root, depth):
            if root is None:
                return 
            if  root.left is None and root.right is None:
                if depth > self.max_d:
                    self.node = root.val
                    self.max_d = depth
            
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        
        dfs(root, 0)
        return self.node

                