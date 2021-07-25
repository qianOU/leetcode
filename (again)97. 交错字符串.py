class Solution:
    # DFS 写的比较难看
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m1, m2, n = len(s1), len(s2), len(s3)
        if m1 + m2 != n: return False
        from functools import lru_cache

        @lru_cache(None)
        def dfs(p1, p2, is_p1=1): # 实际上是不需要抉择该轮到谁了，只要保证之前的是交错字符串即可，下一个字符无论来自谁都是交错字符串
            cur = p1 + p2
            if cur == m1 + m2: return True
            cur = p1 + p2
            prev_p1, prev_p2 = p1, p2
            if is_p1:
                while p1 < m1 and s1[p1] == s3[cur]:
                    p1 += 1
                    cur += 1
                for j in range(p1,  prev_p1, -1):
                    if dfs(j , p2, 0): return True
            
            else:
                while p2 < m2 and s2[p2] == s3[cur]:
                    p2 += 1
                    cur += 1
                for j in range(p2,  prev_p2, -1):
                    if dfs(p1 , j, 1): return True
        
        return dfs(0, 0, 1) or dfs(0, 0, 0)
    
    # 优美的递归写法：
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m1, m2, n = len(s1), len(s2), len(s3)
        if m1 + m2 != n: return False

        from functools import lru_cache
        @lru_cache(None)
        def dfs(p1, p2): # dfs 每次只走 p1 或者 p2 的一步
            cur = p1 + p2
            if cur == m1 + m2: return True
            if p1 < m1 and s1[p1] == s3[cur] and dfs(p1+1, p2): return True
            if p2 < m2 and s2[p2] == s3[cur] and dfs(p1, p2+1): return True
            return False

        return dfs(0, 0)
    
    # 动态规划
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m1, m2, n = len(s1), len(s2), len(s3)
        if m1 + m2 != n: return False
        # dp[i][j] 表示的是 s1[0..i-1] 和 s2[0...j-1] 可以构成交错字符串
        dp = [[False]*(1+m2) for i in range(1 + m1) ]
        # base case 
        dp[0][0] = True
        for i in range(1, m1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1, m2+1):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1] 

        for i in range(1, m1+1):
            for j in range(1, m2 + 1):
                cur = i + j - 1
                dp[i][j] = (s1[i-1] == s3[cur] and dp[i-1][j]) or \
                            (s2[j-1] == s3[cur] and dp[i][j-1])

        return dp[m1][m2]