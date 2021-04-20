# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if root is None:
            return 0
        
        count = 0

        # 后序遍历
        # 递归函数用意：
        # 返回 以 root 为 根节点的左子树叶子节点，以及右子树叶子节点 与 root 的距离小于 distance 的 所有 路径长度
        # 即可能通过 root 作为转折点的 叶子集合
        def dfs(root):
            nonlocal count
            ans = []
            if root is None:
                return []
            
            if root.left is None and root.right is None:
                return [0]
            
            l_leafs = dfs(root.left) # 到 root.left 的距离
            r_leafs = dfs(root.right)# 到 root.right 的距离

            ans.extend(i+1 for i in l_leafs if i<distance)
            ans.extend(i+1 for i in r_leafs if i<distance)

            for i in l_leafs:
                for j in r_leafs:
                    if i + j <= distance-2: # 由于root.left 以及 root.right 到 root的距离各为 1，因此 如果左边叶子节点与右边叶子节点的距离小于等于distance， 即 i + j +2 <= disttance
                        count += 1
            
            return ans
        

        dfs(root )
        return count