# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        if K == 0:
            return [target.val]

        ans = []
        def dfs(root):
            flag = 0 # 标志是否需要剪枝
            if root is None:
                return [] 
            
            res = [] # 存储 以 root 为 根的树，每一个孩子节点与其的距离 【距离小于K的节点】

            left = dfs(root.left)
            right = dfs(root.right)
            
            # 希望 left 中 存有子树节点，便于后序 处理的统一性
            if target.val not in set(i[1] for i in left):
                left, right = right, left

            for l_i,l_j in left: #l_i 是距离 root 的距离， l_j 是子树中想对于的点
                if l_j == target.val:
                    flag = 1 # 标志是否需要剪枝
                    if l_i == K-1: # 情况二： 如果 与 target 距离 等于 k的节点在target 和 根节点的路径之上时
                        ans.append(root.val)
                    for r_i, r_j in right:
                        if r_i + l_i == K-2: # 情况三： 如果 与 target 距离 等于 k的节点在 根节点的另一棵子树上时
                            ans.append(r_j)
                        
                        

            # 情况一：如果 是 target 为根节点的子树
            if root is target:
                ans.extend(i[1] for i in left if i[0]==K-1)
                ans.extend(i[1] for i in right if i[0]==K-1)
                # 只需要将 target 回溯即可
                return [[0, target.val]]

            if not flag:
                # 除了更新子树，也要更新当前遍历节点设为 [0, root.val] 再回溯
                res = [[0, root.val], *[[i[0]+1, i[1]] for i in left if i[0]<K-1], *[[i[0]+1, i[1]] for i in right if i[0]<K-1]]
            else: # 剪枝，只返回有 target 节点的那棵子树结果
                res = [[0, root.val], *[[i[0]+1, i[1]] for i in left if i[0]<K-1]]
 
            
            return res
        
        dfs(root)
        return ans