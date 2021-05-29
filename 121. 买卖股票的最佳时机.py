class Solution:
    # 方法1 : 使用栈来维护递增栈的极值
    def maxProfit(self, prices) -> int:
        stack = []
        profit = 0
        for i in prices:
            while stack and stack[-1] > i:
                profit = max(profit, stack[-1]- stack[0]) 
                stack.pop()
            stack.append(i)
        
        if stack:
            profit = max(profit, stack[-1]- stack[0]) 
        
        return profit

    # 方法2 : 动态规划
    def maxProfit(self, prices) -> int:
        n = len(prices)
        dp = [0]*n # dp[i] 表示在 第 i 天卖出能获得的最大利润 也就是 dp[i] = prices[i] - minvalue
        for i in range(1, n):
            # dp[i-1] = prices[i-1] - minvalue  => minvalue = price[i-1] - dp[i-1]
            dp[i] = max(dp[i-1]+prices[i]-prices[i-1], 0) # 0 表示在 第i 天买入和卖出，前面部分表示在 i-1 之前买入

        return max(dp)
print(Solution().maxProfit([2,1,2,1,0,1,2]))