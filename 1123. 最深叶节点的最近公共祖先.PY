# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 后序遍历
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.max_d = -1
        self.record = []
        def dfs(root, max_d):
            if root is None:
                return 
            if root.left is None and root.right is None:
                if self.max_d < max_d:
                    self.max_d = max_d
                    self.record = [root.val]
                elif self.max_d == max_d:
                    self.record.append(root)
            
            dfs(root.left, max_d+1)
            dfs(root.right, max_d+1)

        dfs(root, 0)
        if len(self.record) == 1:
            return self.record[0]
        
        def lastnode(root):
            if root is None:
                return
            if root.val in [i.val for i in self.record]:
                return root
            
            left = lastnode(root.left)
            right = lastnode(root.right)

            if left is not None and right is not None:
                    return root

        return [lastnode(root), *self.record]