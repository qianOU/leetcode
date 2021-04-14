# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        stack = [root]
        ans = []
        while stack:
            top = stack.pop()
            if  top:
                stack.append(top.left)
                stack.append(top.right)
                ans.append(top.val)

        return ans[::-1]
                
