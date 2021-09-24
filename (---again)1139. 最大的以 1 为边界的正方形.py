class Solution:
    # 暴力
    def largest1BorderedSquare(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        def check(k): # 子正方形的边长
            if k == 0: return True
            for i in range(m-k+1):
                for j in range(n-k+1):
                    tmp = grid[i][j]
                    for s in range(k):
                        tmp &= grid[i+s][j] & grid[i][j+s] & grid[i+k-1][j+s] & grid[i+s][j+k-1]
                        if not tmp: 
                            break
                    if tmp: return True
            return False

        for l in range(min(m, n), -1, -1):
            if check(l): break
        return l**2

class Solution:
    # 动态规划解法
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dp[i][j][0] 表示的是第 i 行，j 列，行方向连续1的个数
        # dp[i][j][1] 表示的是第 i 行，j 列，列方向连续1的个数
        dp = [[[0, 0] for i in range(1+n)] for _ in range(1+m)]
        for i in range(1, 1+m):
            for j in range(1, 1+n):
                if grid[i-1][j-1] == 0: continue
                dp[i][j][0] = dp[i][j-1][0] + 1
                dp[i][j][1] = dp[i-1][j][1] + 1

        ans = 0
        # 从子正方形的右下角开始搜索
        for i in range(1, 1+m):
            for j in range(1, 1+n):
                # 循环的下边界改为 已知的最大边长
                for length in range(min(dp[i][j]), ans, -1): # 从最大可能的边长开始搜索
                    tmp = dp[i-length+1][j-length+1]
                    # 查看正方形的左边长是否满足大于等于 length 也就是判断dp[i][j-length+1][1] 是否大于length
                    if dp[i][j-length+1][1] >= length and dp[i-length+1][j][0] >= length :
                        ans = max(ans, length)
                        break
        return ans ** 2

        
print(Solution().largest1BorderedSquare([[1,1,0,0]]))