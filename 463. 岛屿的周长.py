class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [[0, -1], [0, 1], [1, 0], [-1, 0]] # 控制搜寻方向的
        def countone(i, j):
            count = 4
            for r, h in d:
                x = i + r
                y = j + h
                if 0<=x<m and 0<=y<n:
                    count -= grid[x][y]
            return grid
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans += countone(i, j)
        
        return ans