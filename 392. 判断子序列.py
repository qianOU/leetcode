class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 使用堆栈
        stack = list(t[::-1])
        p = 0
        while stack:
            if s[p] == stack.pop():
                p += 1
            # stack.pop()
        return p == len(s)

    # 基于动态规划 DP
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        dp = [[n]*26 for i in range(n + 1)]
        # dp[i][j] 表示 t[i...] 中首次出现字母 j 的索引位置
        
        for i in range(n-1, -1, -1):
            for j in range(26):
                if t[i] == chr(ord('a') + j):
                    dp[i][j] = i # 如果 t[i] == j, 表明 dp[i][j] = i
                else:
                    dp[i][j] = dp[i+1][j] # 如果 t[i] != j, 也就意味着 dp[i][j] == dp[i+1][j]
        
        print(dp)

        start = 0
        for i in s:
            col = ord(i) - ord('a')
            if dp[start][col] == n:
                return False
            start = dp[start][col] + 1 # 加一别忘记了，表示在 t 中匹配的字符index加一，才是下一次的搜索范围
        
        return True

A = Solution()
print(A.isSubsequence(
"aaaaaa",
"bbaaaa"))