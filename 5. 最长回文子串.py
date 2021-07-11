class Solution:
    # 动态1规划解法 复杂度是O(N2)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # dp[i][j] 表示的是 i 开头 j 结尾 的最长回文子串
        dp = [['']*n for i in range(n)]
        ans, res = 1, s[0]
        # base - case
        for i in range(n):
            dp[i][i] = s[i]
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if dp[i+1][j-1] is not None and s[i] == s[j]:
                    dp[i][j] = s[i] + dp[i+1][j-1] + s[i]
                    if len(dp[i][j]) > ans:
                        ans = len(dp[i][j])
                        res = dp[i][j]
                else:
                    dp[i][j] = None # 代表以 i 为 首 j 为 尾的子串是不存在的
        return res
    
    # 思路2： 中心拓展方法 (最差的时候时间复杂度是O(N2))
    # 回文串的中心只有两种情况，奇数时中心是 一个字符， 偶数长度时，中心是两个相同字符
    # 我们可以对上述两种中心情况分别进行尝试
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # 返回以 center1，以及 center2 为中心的时候，最长回文子串的左右边界
        def extend_bound(center1, center2):
            l, r = center1, center2
            while l >= 0 and r < n and s[l] == s[r]:
                l, r = l - 1, r + 1
            return l+1, r-1
        
        start, end = 0, 0
        for i in range(n):
            l1, r1 = extend_bound(i, i) # 以 i 为中心的情况
            l2, r2 = extend_bound(i, i+1)  # 以 i, i + 1 为中心的情况
            if r1 - l1 > end - start:
                end, start = r1, l1
            if r2 - l2 > end - start:
                end, start = r2, l2
        
        return s[start: end+1]
                
            