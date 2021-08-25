class Solution:
    # 动态规划
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [[0, 0] for i in range(1+n)] # dp[i]表示的是以s[i]为结尾其为j状态下，最小翻转次数

        for i in range(1, 1+n):
            if s[i-1] == '0':
                dp[i][0] = dp[i-1][0]
                dp[i][1] = min(dp[i-1]) + 1
            else:
                dp[i][1] = min(dp[i-1])
                dp[i][0] = dp[i-1][0] + 1
        print(dp)
        return min(dp[-1])

print(Solution().minFlipsMonoIncr("00110"))