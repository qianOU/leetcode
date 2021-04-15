# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def dfs(root):
            if root is None:
                return

            # 判别是否是 0 的叶子节点
            if root.val == 0 and root.left is None and root.right is None:
                return None

            left = dfs(root.left)
            right = dfs(root.right) 



            root.left = left
            root.right = right

            # 由于可能存在连续的 0 节点，所以这里需要对减去 0的叶子节点，进行判断是否依然是0的叶子节点
            if root.val == 0 and root.left is None and root.right is None:
                return None
            return root

        return dfs(root)