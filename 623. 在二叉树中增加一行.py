# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        def dfs(root, cur, state): # state 为 0 代表操作左子树
            if not root:
                # 对于叶子节点进行处理
                if depth == cur:
                    node = TreeNode(val)
                    if state:
                        node.right = root
                    else:
                        node.left = root
                    
                    return node
        
                return 
            # 对于 根节点操作
            if depth == 1:
                node = TreeNode(val)
                node.left = root
                return node

            left = dfs(root.left, cur+1, 0)
            right = dfs(root.right, cur+1, 1)

            root.left = left
            root.right = right

            if cur == depth:
                node = TreeNode(val)
                if state:
                    node.right = root
                else:
                    node.left = root
                
                return node
            
            return root
        return dfs(root, 1, 0)
