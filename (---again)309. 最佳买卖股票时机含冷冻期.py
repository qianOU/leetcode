class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # j：0 持有， 1 不持有在冷冻期  2： 不持有不在冷冻期
        # dp[i][j] 表示的是在 第 i 天，在 j 状态下，获得的最大利益
        dp = [[0, 0, 0] for i in range(n)]
        # base case
        dp[0][0] = -prices[0]

        for i in range(1, n):
            # 第 i 天 持有
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            # 第 i 天 不持有且在冷冻期，也就是表明 在 第 i 天出售了股票
            dp[i][1] = dp[i-1][0] + prices[i]
            # 第 i 天，不持有股票且不在冷冻期，也就说明 第 i 天不持有股票没交易
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        
        return max(dp[n-1])