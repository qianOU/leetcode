# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 后序遍历查看是否除了根节点之外，有子树的节点数大于 1 号选手
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def dfs(root):
            