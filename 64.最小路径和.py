class Solution:
    # 动态规划 可以进一步优化空间复杂度
    def minPathSum(self, grid) -> int:

        m, n = len(grid), len(grid[0])
        # 表示走到 i, j 的最小花费
        dp = [[0]*n for i in range(m)]
        # base-case 
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]


        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]



        

print(Solution().minPathSum( [[1,2,3],[4,5,6]]))
