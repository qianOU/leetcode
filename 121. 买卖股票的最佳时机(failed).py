class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [0]*n # dp[i] 表示  第j天卖出股票能获得的最大利润
        # base - case dp[-1] = 0
        
        for i in range(1, n):
           
        return res

print(Solution().maxProfit([2,4,1]))