class Solution:
    # 动态规划
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0]*(1+n) # dp[i] 表示到达 i 的时候，能获得的最大利益
        adj = [[] for i in range(1+n)]
        for i, j, v in rides:
            adj[j].append((i, v)) # 能够到达 j 的所有顾客

        for i in range(1, 1+n):
            dp[i] = dp[i-1] # 不接受在 i 时刻下车的客人
            for j, v in adj[i]: # 接受在 i 时刻下车的顾客，选择最大利益的人
                dp[i] = max(dp[i], dp[j] + i - j + v)
        return dp[n]