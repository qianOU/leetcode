class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        check = lambda x, y: 0<=x<m and 0<=y<n

        visited = set()

        # 从 i，j处开始向四个方向进行搜索， i,j 是陆地
        def dfs(i, j):
            count = 1
            visited.add((i,j))
            for l, r in d:
                if check(i+l, j+r) and (i+l, j+r) not in visited:
                    if  grid[i+l][j+r]:
                        count += dfs(i+l, j+r)
            return count

        max_ = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i,j) not in visited: # 只有 i, j 是陆地，并且 没有探索过才进行搜索最大陆地
                    item = dfs(i, j)
                    max_ = max(max_, item)
        
        return max_

            
print(Solution().maxAreaOfIsland([[0]]))

print(Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))