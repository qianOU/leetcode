class Solution:
    # 动态规划
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*(n+1) for i in range(m+1)]
        # base-case
        dp[1][1] = int(obstacleGrid[0][0] != 1)

        for i in range(1, m+1):
            for j in range(1, n+1):
                if not obstacleGrid[i-1][j-1]:
                    if i == j == 1: continue
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                
        return dp[m][n]


print(Solution().uniquePathsWithObstacles(
[[0,0,0],[0,1,0],[0,0,0]]))