class Solution:
    # 动态规划 dp 数组中的 状态定义十分重要
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * n # 构造矩阵的一行， dp[i] 表示以 i 为终点的 连续 1 的个数
        
        ans = 0
        for row in range(m):
            for j in range(n):
                dp[j] = 0 if not matrix[row][j] else dp[j] + 1
            
            tmp = sorted(dp)
            for j in range(n-1, -1, -1):
                ans = max(ans, tmp[j]*(n-j))

        return ans

