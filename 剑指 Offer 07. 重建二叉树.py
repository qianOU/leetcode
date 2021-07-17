# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        

        def dfs(cur, l ,r):
            if l >= r:
                return cur, None
            
            for i in inorder[l: r]:
                if i == preorder[cur]:
                    break
                    
            node = TreeNode(cur)
            cur += 1
            nxt, node.left = dfs(cur+1, 0, i)
            node.right = dfs(nxt+1，i+1, r)
            return node
        
        return dfs(0, 0, len(inorder))
