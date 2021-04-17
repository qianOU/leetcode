# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 前序遍历
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:

        def compare(r1_l, r1_r, r2_l, r2_r):
            tmp1 = [r1_l,] if not r1_l else [r1_l.val]
            tmp1.append(r1_r if  not r1_r else r1_r.val)
            tmp2 = [r2_l,] if not r1_2 else [r2_l.val]
            tmp1.append(r2_r if  not r2_r else r2_r.val)
            return 

        def dfs(root1, root2):
            if root1 is None and root2 is None:
                return True
            
            if root1.val != root2.val:
                return False
            else:
                root1.left