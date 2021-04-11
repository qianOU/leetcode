
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 中序遍历 + 有序字典 缺点是必须遍历完整的 BST
    def findTarget(self, root: TreeNode, k: int) -> bool:
        from collections import OrderedDict
        res = OrderedDict()
        
        def traverse(root):
            if root:
                traverse(root.left)
                res[root.val] = res.get(root.val, 0) + 1
                traverse(root.right)
        traverse(root)

        if res.get(k/2, 0) >= 2:
            return True

        for i in res:
            if i > k//2:
                return False
            if res.get(k-i, 0)>0:
                return True 

    # 前序dfs + set set里面记录的是已经遍历过的点 + yield 生成器
    def findTarget(self, root: TreeNode, k: int) -> bool:
            
            res = set()
            
            def traverse(root):
                if root:
                    if k - root.val in res:
                        yield True
                    res.add(root.val)
                    yield from traverse(root.left)
                    yield from traverse(root.right)
            
            gen = traverse(root)
            
            try:
                gen.send(None)
            except  StopIteration:
                return False
            else:
                return True
