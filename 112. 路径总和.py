# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS 
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        def dfs(root, sum_=0):
            if root:
                # 到达叶子节点
                if root.left is None and root.right is None and sum_ + root.val == targetSum:
                    return True
                sum_ += root.val
                if dfs(root.left, sum_):
                    return True
                if dfs(root.right, sum_):
                    return True
            
        return bool(dfs(root))
    # BFS
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        
        q = [root]
        ans = [0]

        while q:
            node = q.pop(0)
            v = ans.pop(0)
            # 判别是否走到了叶子节点
            if node.left is None and node.right is None:
                if v+node.val == targetSum:
                    return True
            if node.right is not None:
                q.append(node.right)
                ans.append(v+node.val)
            if node.left is not None:
                q.append(node.left)
                ans.append(v+node.val)
        
        return False