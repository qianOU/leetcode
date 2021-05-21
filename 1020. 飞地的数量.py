class Solution:
    def numEnclaves(self, grid) -> int:
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        check = lambda x, y: 0<x<m-1 and 0<y<n-1
        visited = set()
        isboarder = lambda x, y: x in (0, m-1) or y in (0, n-1)

        def dfs(i, j):
            flag = False
            count = 1
            for l, r in d:
                x, y =i+l, j+r
                if check(x, y) and (x, y) not in visited and grid[x][y]:
                    visited.add((x, y))
                    one = dfs(x, y)
                    if not one:
                        flag  = 1
                    else:
                        count += one
                elif isboarder(x, y) and  grid[x][y]: # 可以走出边界
                    print('----', x, y, grid[x][y])
                    flag = 1
            
            return count if not flag else 0
            
        
            

        count = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] and (i, j) not in visited:
                    visited.add((i, j))
                    count += dfs(i, j)

        return count
    

print(Solution().numEnclaves(
    [[0,0,1,1,1,0,1,1,1,0,1],[1,1,1,1,0,1,0,1,1,0,0],[0,1,0,1,1,0,0,0,0,1,0],[1,0,1,1,1,1,1,0,0,0,1],[0,0,1,0,1,1,0,0,1,0,0],[1,0,0,1,1,1,0,0,0,1,1],[0,1,0,1,1,0,0,0,1,0,0],[0,1,1,0,1,0,1,1,1,0,0],[1,1,0,1,1,1,0,0,0,0,0],[1,0,1,1,0,0,0,1,0,0,1]]
))