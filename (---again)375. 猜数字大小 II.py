class Solution:
    # 存在子问题
    # 递归需要 n！ 复杂度
    # 这种最坏情况下，考虑的问题，都具有独立子问题特性。 2 维dp问题
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] 表示 猜测 区间[i, j] 在最坏情况下需要的最少金额数
        dp = [[0]*(1+n) for i in range(1+n)]
        # base case
        # 区间长度为 1 的时候，不需要再花费金钱查询
        for i in range(1+n):
            dp[i][i] = 0
        
        for i in range(n, 0, -1):
            for j in range(i+1, n+1):
                # 去除区间最右边元素
                dp[i][j] = dp[i][j-1] + j
                for p in range((i+j)//2, j): # 优化，p 可以缩小到 二分的右半部分，因为二分后最坏的情况就是落在二分的右半部分
                    dp[i][j] = min(dp[i][j], max(
                        dp[i][p-1],
                        dp[p+1][j]
                    ) + p)
        return dp[1][n]