# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        if root is None:
            return 
        ans = []
        def zhong(root):
            if root is None:
                return
            
            zhong(root.left)
            ans.append(root)
            zhong(root.right)
        
        zhong(root)
        for i in range(len(ans)-1):
            ans[i].right = ans[i+1]
            ans[i].left = None
        
        return ans[0]