# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 当前节点有 k + 1 个状态，表示当前节点是第几个染色下其子树最大价值
    def maxValue(self, root: TreeNode, k: int) -> int:
        # 后序遍历 + 动态规划
        # 放回的是 root 的 dp 状态表
        def dfs(root):
            dp = [0]*(1+k) # dp[i] 表示的是 root 是 染色i个节点的情况下其子树最大的价值和是多少
            if root is None: return dp
            left = dfs(root.left)
            right = dfs(root.right)
            # root 不染色，下其子树最大价值，左右子树之和
            dp[0] = max(left) + max(right)
            # 枚举染色数量 i 
            for i in range(1, 1+k):
                # 罗列root是第几个被染色的情况
                dp[i] = max(left[l] + right[i-1-l] for l in range(i)) + root.val
        
            return dp
        
        return max(dfs(root))