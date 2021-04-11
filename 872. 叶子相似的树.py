# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # 普通的 dfs
        def dfs(root, path):
            if root:
                if root.left is None and root.right is None:
                    path.append(root)
                else:
                    dfs(root.left, path)
                    dfs(root.right, path)
            
        a = []
        b = []
        dfs(root1, a)
        dfs(root2, b)
        # print(a, b)
        return a==b

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # 基于协程概念的 dfs
        def dfs(root):
            if root:
                if root.left is None and root.right is None:
                    yield root.val
                else:
                    yield from dfs(root.left, path)
                    yield from dfs(root.right, path)
            

        return list(dfs(root1)) == list(dfs(root2))