# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 回溯
    def longestZigZag(self, root: TreeNode, depth) -> int:
        max = 0
        def dfs(root, state, depth):
            # state 1 表示走的左子树
            # state 0 表示走的右子树
            nonlocal max
            if root is None:
                return 
            
            if (not root.left or (root.left and state)) and  \
                 (not root.right or (root.right and not state)):
                   if  max < depth:
                       max = depth 

            if root.left and not state:
                dfs(root.left, 1, depth+1)
            elif root.left:
                dfs(root.left, 1, 0)
            if root.right and state:
                dfs(root.right, 0, depth+1)
            elif root.right:
                dfs(root.right, 0, 0)
        

    
            

