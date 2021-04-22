# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        # 检查 s 和 t 子树是否相等
        def check(s, t):
            if s is None and t is None:
                return True
            if s is None or t is None:
                return False
            
            return s.val == t.val and check(s.left, t.left) and check(s.right, t.right)
        
        if check(s, t): # 如果 S 与 t 相等 返回 True
            return True
        
        if s is None:
            return False
            
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) # 否则检查 s 的 左/右子树 是否 与 t 相等