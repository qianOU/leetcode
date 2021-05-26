# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 后序遍历
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        
        def dfs(root, count):
            if not root:
                return

            item = count + root.val
            if root.left is None and root.right is None:
                if item < limit:
                    return item, None
                return item, root
            
            left, root.left = dfs(root.left, count+root.val)
            right, root.right = dfs(root.right, count+root.val)

            if left < limit and right < limit:
                return None

            return root
        

            