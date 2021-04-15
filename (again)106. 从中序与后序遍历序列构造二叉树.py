# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        map_index = dict(i[::-1] for i in enumerate(inorder))
        def fenzhi(l_i, r_i):
            
            if l_i > r_i:
                return 

            root = TreeNode(postorder.pop())
            idx = map_index.get(root.val)
            root.right = fenzhi(idx+1, r_i)
            root.left = fenzhi(l_i, idx-1)
            return root
        return fenzhi(0, len(inorder)-1)