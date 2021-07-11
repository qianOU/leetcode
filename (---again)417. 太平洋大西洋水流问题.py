class Solution:
    # 对于每个点 流入 大西洋 还是太平洋，判别法则是一致的
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        status1 = [[0]*n for i in range(m)] # 是否能流入 大西洋 
        status2 = [[0]*n for i in range(m)] # 是否能流入 太平洋
        d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # 从边界开始， DFS 搜索 能到达 此处 位置的 高位，将其相应的 status 置为 1
        def dfs(r, c, status):
            status[r][c] = 1 # 改变状态为 1，即可到达某一处海洋
            for i, j in d:
                x, y = r + i, j + c
                if 0 <= x < m and 0 <= y < n \
                and heights[x][y] >=  heights[r][c] and not status[x][y]:
                    dfs(x, y, status)
        # 边界
        for i in range(m):
            dfs(i, 0, status1)
            dfs(i, n-1, status2)
        
        for i in range(n):
            dfs(0, i, status1)
            dfs(m-1, i, status2)

        ans = []
        for i in range(m):
            for j in range(n):
                if status2[i][j] and status1[i][j]:
                    ans.append([i, j])
        
        return ans
