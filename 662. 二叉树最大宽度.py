# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 完全二叉树， 可以与二进制结合进行考虑
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return
        
        q1 = [root]
        q2 = [1]
        
        max_len = 0

        while q1:
            sz = len(q1)
            max_len = max(q2[-1] - q2[0]+1, max_len)
            for i in range(sz):
                top = q1.pop(0)
                code = q2.pop(0)
                if top.left:
                    q1.append(top.left)
                    q2.append(code<<1)
                if top.right:
                    q1.append(top.right)
                    q2.append((code<<1) + 1)
        
        return max_len