class Solution:
    # 完全背包问题
    def change(self, amount: int, coins: List[int]) -> int:
 
        n = len(coins)

        # dp[i][j] 表示的是 只是使用 前 i 枚 硬币 的时候， 可以凑成 j 金额的方案数
        dp = [[0]*(amount+1) for i in range(1+n)]
        # base-case
        for i in range(1+n):
            dp[i][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                # 两种情况：是否要将 coins[i-1]，纳入方案中
                # 不放入 : dp[i-1][j] 即用前 i-1 件物品 来 构成 j 的方案数
                # 放入： dp[i][ j - coins[i-1] ]  由于可以无限使用 i枚硬币，因此在 前 i 枚硬币中继续找寻 j - coins[i-1] 的金额数
                # 综上，dp[i][j] 是上述两个方案的和
                
                dp[i][j] = dp[i-1][j] # 对应不放入 
                if j - coins[i-1] >= 0: # 如果可以放入
                    dp[i][j] += dp[i][j-coins[i-1]]
        
        return dp[n][amount]