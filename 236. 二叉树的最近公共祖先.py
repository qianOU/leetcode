# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 后序遍历 可以拿到 最近公共祖先
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        if root.val in (p.val, q.val):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left is None and right is None:
            return # 无公共祖先
        elif left is None:
            return right # 只有右子树有匹配结果，回溯返回 右子树匹配的值
        elif right is None:
            return left # 只有左子树有匹配结果，回溯返回 左子树匹配的值
        else: 
            return root # 如果左子树 与 右子树 分别匹配一项，则 root是最近公共祖先， 不断回溯最近公共祖先
    
        