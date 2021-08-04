from pprint import pprint

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[1]*n for i in range(n)]
        # base case
        for i in range(n): dp[i][i] = 1
        ans = n
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                ans += dp[i][j]
        return ans

print(Solution().countSubstrings(
'aaaa'
))