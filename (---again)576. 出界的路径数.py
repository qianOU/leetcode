class Solution:
    # 直接递归 + 记忆化优化
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]    
        

        from functools import lru_cache
        @lru_cache(None)
        def dfs(i,j, count): # 从 i,j 出发最多走 count步有多少条路径
            total = 0
            if count < 0:
                return 0
            if i < 0 or i >= m or j<0 or j>=n:
                    return 1
            for l, r in d:
                x, y = i+l, j+r
                total += dfs(x, y, count-1) % (10**9+7)
            
            return total % (10**9+7)

        return dfs(startRow, startColumn, maxMove)

    # 动态规划
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]    
        check = lambda x, y: 0 < x < m-1 and 0 < y < n-1

        # dp[i][j] 表示在 x 步的限制下，有dp[i][j] 种走法可以到达 (i,j)
        dp = [[0]*n for i in range(m)]
        # base-case  走 0  次的时候 dp[startRow][startColumn] = 1
        dp[startRow][startColumn] = 1
        res = 0
        mod = 10**9 + 7 

        # 一共 走 n 步
        for k in range(1, maxMove+1):
            tmp = dp.copy()
            dp =  [[0]*n for i in range(m)]
            for i in range(m):
                for j in range(n):
                    for l, r in d:
                        x, y = i+l, j+r
                        if 0<=x<m and 0<=y<n:
                            dp[i][j] += tmp[x][y]
                        else: #如果（i，j）第 k 步能走出某个边界，则从这个边界出去的路径一共有 tmp[i][j] 条，即 第 k-1次到达 i,j的路径数
                            res += tmp[i][j]
                        
                    dp[i][j] %= mod

                    res %= mod

        return res


print(Solution().findPaths(1,3,3,0,1))