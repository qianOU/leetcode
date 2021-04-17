# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        self.cur_depth = -1 # 记录当前位于的数的深度
        def dfs(root, res, depth):
            if root is None:
                return
            # 只有当下一层的深度 大于 我们的当前深度时，才将值放入记录数组中
            if depth > self.cur_depth:
                res.append(root.val)
                self.cur_depth += 1 # 对于 depth层只放一个值，即改变我们的当前层位置
            
            dfs(root.right, res, depth+1) # 首先遍历右子树，找寻符合的点
    
            dfs(root.left,res, depth + 1) #其次再遍历左子树
        
        ans = [] #答案数组
        dfs(root, ans, 0) # 0 代表根节点的深度
        return ans
