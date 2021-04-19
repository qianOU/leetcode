# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def dfs(root):
            if root is None:
                return
            
            if key < root.val:
                root.left = dfs(root.left)
            if key > root.val:
                root.right = dfs(root.right)
            if key == root.val:
                if root.left:
                    temp = root.left
                    prev = root.left
                    while temp.right:
                        prev = temp
                        temp = temp.right
                    root.val = temp.val
                    prev.right = None

                    return root
                else:
                    return root.right
            
        return dfs(root)

