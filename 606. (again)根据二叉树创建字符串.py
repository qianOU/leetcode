# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t) -> str:
        
        def tranverse(root):
            # 当是空节点时，返回空字符串
            if root is None:
                return ''
            # 当无孩子结点时
            if root.left is None and root.right is None:
                return str(root.val)
            # 当只有右子节点时
            if root.right:
                left = tranverse(root.left)
                right = tranverse(root.right)
                return  str(root.val) + '(%s)' % left + '(%s)' % right
            # 当只有左子节点的时候
            left = tranverse(root.left)
            return str(root.val) +  '(%s)' % left 
            
            
        return tranverse(t)
        