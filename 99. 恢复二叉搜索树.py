# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 
        
        prev = TreeNode(float('-inf'))
        self.ans = [] # 0(1) 的复杂度,最多存放两个元素
        # 中序遍历
        def dfs(root):
            nonlocal prev
            if root is None:
                return 
            dfs(root.left)
            if prev.val > root.val:
                self.ans.append((prev, root))  # 记录不符合递增顺序的一组关系点 
            prev =   root # 更新 上一个中序遍历的值
            dfs(root.right)
        
        dfs(root)
        if (len(self.ans)) == 2: #需要交换位置的两个点在中序遍历时处于不同位置
            self.ans[0][0].val, self.ans[1][-1].val = self.ans[1][-1].val,  self.ans[0][0].val
        else: # 需要交换的两个点在中序遍历的时候处于相邻位置
            self.ans[0][0].val, self.ans[0][-1].val = self.ans[0][-1].val, self.ans[0][0].val