# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        records = []
        def dfs(root, depth):

            if len(records) <= depth:
                records.append([])
            if root is None:
                records[depth].append('')  
                      
            dfs(root.left, depth+1)
            records[depth].append(str(root.val))
            dfs(root.right, depth+1)
            
        dfs(root, 0)
        return records
            
