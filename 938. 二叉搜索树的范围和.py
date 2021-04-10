# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum_ = 0
        def tranvse(root):
            nonlocal sum_
            if root is None:
                return 
            
            if root.val < low:
                tranvse(root.right)
                return 
            # 中序遍历, BST的中序遍历是一个递增序列
            tranvse(root.left) 
            if low<= root.val<=high:
                sum_ += root.val
            elif root.val > high: # 超过最高范围直接停止遍历,右子树
                return 
            tranvse(root.right)
        
        tranvse(root)
        return sum_
