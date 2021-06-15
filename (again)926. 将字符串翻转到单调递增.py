class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        # dp[i][j] 表示 在 i 位置的时候，其为 j 状态的时候，保持单调的最小翻转的次数
        dp = [[0,0] for i in range(n+1)]

        for i in range(n):
            if s[i] == '0':
                dp[i+1][0] = dp[i][0]
                dp[i+1][1] = min(dp[i][0], dp[i][1]) + 1
            else:
                dp[i+1][1] = min(dp[i][0], dp[i][1])
                dp[i+1][0] = dp[i][0] + 1

        print(dp)  
        return min(dp[n])

print(Solution().minFlipsMonoIncr(
"0101100011"))