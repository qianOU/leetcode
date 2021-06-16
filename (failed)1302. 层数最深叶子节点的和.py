# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return

        q = [root]
        while  q:
            sz = len(q)
            total = 0
            for _ in range(sz):
                node = q.pop(0)
                total += node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return total

    # dfs 递归
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # 两个全局变量
        self.max_depth = -1 # 记录最深的层数
        self.total = 0 # 记录最深层的节点值之和
        def dfs(root, depth=0):
            if root is None:
                return
            if depth > self.max_depth: # 如果当前层数大于记录的最大层数
                self.max_depth, self.total = depth, root.val
            
            if depth == self.max_depth: # 如果当前层数与记录中的最大层数相等时
                self.total += root.val 

            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        
        dfs(root)
        return self.total