# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalanced(self, root: TreeNode) -> bool:   

        # 后序遍历 获得当前节点位于的树的深度（叶子节点深度为 1）
        def back_traverse(root):
            if root is  None:
                return 0
            
            l_p = back_traverse(root.left)
            r_p = back_traverse(root.right)
            if l_p < 0 or r_p < 0 or  abs(l_p-r_p) > 1:
                return -1
            
            return max(l_p, r_p) + 1 # 当前节点的深度为 左右子节点的深度 + 1

        return back_travese(root) > 0


        # 前序遍历 获得当前节点位于的树的深度
        def tranvese(root, layer):
            if root is None:
                return layer
            
            layer += 1
            left_depth = tranvese(root.left, layer)
            right_depth = tranvese(root.right, layer)
            
            if not self.flag:
                return 
            
            if abs(left_depth - right_depth)  > 1:
                self.flag = False
            return max(left_depth, right_depth)
    
        self.flag = True
        # tranvese(root, 0)
        # return self.flag


