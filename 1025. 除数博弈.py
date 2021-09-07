class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False]*(n+1) # dp[i] 表示当黑板写的是 i 的时候最大话分差能否能赢
        # base case 
        dp[0] = dp[1] = False

        for i in range(2, n+1):
                dp[i] = any(not dp[i-j] for j in range(1, i) if i % j == 0)
        
        print(dp)
        return dp[n]

print(Solution().divisorGame(3))