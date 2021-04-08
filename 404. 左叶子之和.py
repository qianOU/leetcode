# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum_ = 0
        # 前序遍历
        def bt(root):
            nonlocal sum_
            if root is None:
                return
            # 第一个判断条件 确定是 root.left是左节点， 第二个条件判断 root.left 是叶子节点， 综合来看root.left就是左叶子节点
            if root.left is not None and (root.left.left is None and root.left.right is None):
                sum_ += root.left.val
                return 
            
            bt(root.left)
            bt(root.right)

        # bt(root)
        # 后序遍历
        # 后序遍历需要先说明 基本情况为None时，根节点返回值的情况， 在return 时 要写明 递推公式
        def bt(root):
            if root is None:
                return 0

            cur = 0
            if root.left is not None and (root.left.left is None and root.left.right is None):
                cur = root.left.val


            
            return bt(root.left) + bt(root.right) + cur #后序遍历
        return sum_