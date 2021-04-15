# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0 # 记录总发移动量， 为每一个节点负载量的绝对值
        # dfs: 指的是以节点 root 为根节点的过载量,
        # 负载量m为负数表示该节点还差硬币abs(m)个， 为正代表多了 m 个硬币需要供给给其它成员
        # 后序遍历的反式
        def dfs(root):
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans += abs(left) + abs(right)
            return root.val + left + right - 1 # -1 是代表root自身需要使用一个硬币
        
        dfs(root)
        return self.ans

