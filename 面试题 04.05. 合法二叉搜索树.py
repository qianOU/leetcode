# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归写法
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root, l, r):
            if root is None: return True
            return l < root.val <r and dfs(root.left, l, root.val) and dfs(root.right, root.val, r)
    
        return dfs(root, float('-inf'), float('inf'))

    # 迭代写法， 中序遍历的迭代
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        # 将root的完全左子树入栈
        def order(root):
            while root:
                stack.append(root)
                root = root.left
        # 根节点的左子树全部入账
        prev = float('-inf')
        order(root)
        while stack:
            cur = stack.pop()
            if prev >= cur.val: return False
            prev = cur.val
            order(cur.right)
        return True