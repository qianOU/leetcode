# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(root):
            if root is None:
                return


            root.left = dfs(root.left)
            root.right = dfs(root.right)
            # 叶子节点
            if root.left is None and root.right is None:
                if root.val == target:
                    return None
               
                
            return root

        return dfs(root)