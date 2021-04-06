# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_ = 0 # 记录最长路径的变量
        def bt(root, depth):
            """
            记录以 root 为根节点的最大深度
            """
            nonlocal max_
            # base  case
            if root is None:
                return depth

            depth += 1 # 前序遍历
            l = bt(root.left, depth) # 左子树的最高深度
            r = bt(root.right, depth) # 右子树的最高深度

            if l + r - 2*depth > max_: # 查看 以 root 为转折节点，是否是 最长路径
                max_ = l + r - 2*depth
            
            return max(l, r) # 返回 以 root 为根节点 的 最大深度
        
        # bt(root, 0)

        def bt2(root):
            """
            记录以 root 为根节点的最大深度
            # 后序遍历
            """
            nonlocal max_ # 记录的是最长路径经过的节点数
            # base  case
            if root is None:
                return 0

            # 后续遍历
            l = bt2(root.left) # 左子树遍历的节点数
            r = bt2(root.right) # 右子树遍历的节点数

            if l + r + 1 > max_: # 查看 以 root 为转折节点，是否是 最长路径 + 1 代表的是 根节点
                max_ = l + r +  1
            
            return max(l, r) + 1 # 返回 以 root 为根节点 的 深度
        return max_ - 1 # 节点数 - 1 才是 真正的路径长度
        

