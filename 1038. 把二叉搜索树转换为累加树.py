# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        self.total = 0
        # 反序中序遍历
        # 遍历顺序 右 - 中 - 左
        def bt(root):
            if root is None:
                return 
            
            bt(root.right)
            self.total += root.val
            root.val = self.total
            bt(root.left)

        bt(root)

        return root