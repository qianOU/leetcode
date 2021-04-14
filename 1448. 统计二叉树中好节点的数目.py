# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   # dfs
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.total = 0

        def bp(root, res):
            if root is None:
                return 
            if all(i <= root.val for i in res):
                self.total += 1
                

            res.append(root.val)
            if root.left:
                bp(root.left, res.copy())
            if root.right:
                bp(root.right, res)

        bp(root, [])
        return self.total
    
    # 优化的 dfs 
     # 实质就是需要记录 已遍历路径的最大值
     # 所以 直接在每一次遍历的过程中，，将当前节点的值设为已知的最大值
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.total = 0

        def dfs(root):
            if root is None:
                return 
            if not root.left:
                if root.left.val >= root.val:
                    self.total += 1
                else:
                    root.left.val = root.val

            if not root.right:
                if root.right.val >= root.val:
                    self.total += 1
                else:
                    root.right.val = root.val  

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.total + 1
