# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # dfs 自底向上， 暴力
    def smallestFromLeaf(self, root: TreeNode) -> str:
        
        zip_code = {i:chr(97+i) for i in range(26)}
       
        if root is None:
            return ''

        def dfs(root):
            if root is None:
                return []
        
            if root.left is None and root.right is None:
                return [zip_code[root.val]]
            
        
            left = dfs(root.left)
            right = dfs(root.right)

            cur = zip_code[root.val]
            return [*[i+cur for i in left], *[j+cur for j in right]] 
          
        item = dfs(root)

        return min(item)