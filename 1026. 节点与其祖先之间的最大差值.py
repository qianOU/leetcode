# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 实质就是记录当遍历到 叶子节点的时候，路径的最大值与最小值之差
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        self.max = float('-inf')

        # 找寻 以 root 为根节点的子树的 极值
        def dfs(root, min, max):
            if root is None:
                return 
            # 前序遍历
            if root.val < min:
                min = root.val
            if root.val > max:
                max = root.val

            if root.left is None and root.right is None:
                if self.max < max - min:
                    self.max = max-min    
                return
            

            dfs(root.left, min, max)
            dfs(root.right, min, max)

        dfs(root, float('inf'), float('-inf'))  
        return self.max