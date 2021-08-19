class Solution:
    # 思路1： 记忆化 DFS 搜索
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        from functools import lru_cache
        ans = 0
        d = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        steps = [(2, 1), (1, 2)]

        check = lambda x, y: 0<=x<n and 0<=y<n
        @lru_cache(None)
        def dfs(x, y, res=k):
            if res == 0: 
                return 1
            count = 0
            for x1, y1 in steps:
                for i, j in d:
                    step_x, step_y = i*x1, j*y1
                    cur_x, cur_y = x + step_x, y + step_y
                    if check(cur_x, cur_y):
                        count += dfs(cur_x, cur_y, res-1)
            return count
        
        return dfs(row, column, k) / 8**k
    
    # 思路2: 动态规划
    # 原则上是三维dp，不过可以通过循环某个维度来降维dp矩阵
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        d = [(2, -1), (2, 1), (1, -2), (1, 2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
        dp = [[0]*n for i in range(n)] # dp[i][j] 表示的是当马在(i, j) 位置时还在棋盘上的概率
        dp[row][column] = 1 # base case
        check = lambda x, y: 0<=x<n and 0<=y<n
        for i in range(k):
            dp2 = [[0]*n for i in range(n)]# 表示的是当位于 i 步的时候，马在(i, j) 位置时还在棋盘上的概率
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for step_x, step_y in d:
                        cur_x, cur_y = r + step_x, c + step_y
                        if check(cur_x, cur_y):
                            dp2[cur_x][cur_y] += val / 8 # 下一步还在棋盘的概率
            dp = dp2 # 汇总 i 步的结果
        
        return sum(map(sum, dp))


                        


print(Solution().knightProbability(3, 2, 0, 0))