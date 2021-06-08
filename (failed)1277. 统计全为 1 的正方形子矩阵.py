class Solution:
    # 错误的写法
    def countSquares(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        res = [0]*n
        ans = 0
        for i in range(m):
            res = [res[j] + 1 if matrix[i][j] else 0 for j in range(n)]
            j = 0
            while j < n:
                prev = j
                while j < n and res[j] == res[prev] > 0:
                    j += 1
                    ans += 1                

                # 所有 子矩阵的边长 大于 1 的情况
                for p in range(res[prev], 1, -1):
                    ans += j - prev - p +1 
                if j<n and not res[j]: j += 1
            
        return ans
    # 动态规划
    def countSquares(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        #dp[i][j] 表示的是 以 （i,j） 为右下角的矩阵最大边长
        dp = [[0]*n for i in range(m)]
        #base- case
        for i in range(m): dp[i][0] = matrix[i][0]
        for j in range(n): dp[0][j] = matrix[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0: dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        ans = sum(dp[i][j] for i in range(m) for j in range(n))
        return ans

print(Solution().countSquares([[1,0,1],[1,1,0],[1,1,0]]))