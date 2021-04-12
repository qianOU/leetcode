# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS + set
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return False
        
        q = [root]
        
        while q:
            sz = len(q)
            layer = []
            flag = 1
            for i in range(sz):
                node = q.pop(0)
                layer.append(node.val if node is not None else None)
                if flag and x in layer and y in layer:
                    flag = 0 #哨兵，只当 x， y 第一次同时出现在list中，设置
                    idx = i # 第 i 位一定是二者其一
                    if not( idx%2 and layer[idx-1] in (x, y)):
                        return True
                if not node:
                    continue
                q.append(node.left)
                q.append(node.right)
        
        return False
    
    # 递归(前序遍历) + map
 def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
     depth = dict() #记录 值的深度
     parents = {} # 记录值对应的 父亲节点
     
     def dfs(node, parent=None):
         if node:
             depth[node.val] = 1 + depth[parent.val] if parent else 0
             parents[node.val] = parent
             dfs(node.left, node)
             dfs(node.right, node)
        
    dfs(root)
    return depth[x] == depth[y] and parents[x] != parents[y]
