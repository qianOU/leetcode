class Solution:
    def closedIsland(self, grid) -> int:
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        check = lambda x, y: 0<x<m-1 and 0<y<n-1

        visited = set()
        def dfs(i, j):  
            count = 0         
            for l, r in d:
                x, y = i + l, j + r
                if check(x, y) and (x,y) not in visited and not grid[x][y]:
                    visited.add((x, y))
                    if dfs(x, y): # 如果 沿着 x，y 方向是封闭的就会返回1， 那么 对于当前来说这一侧的搜索 也是 封闭的因此 count + 1
                        count += 1
                
                elif (x,y) in visited or grid[x][y]:
                    count += 1

            if count == 4:
                return 1    
                
            return 0
        
        num = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if (i, j) not in visited and not grid[i][j]:
                    visited.add((i, j))
                    num += dfs(i, j)
        
        return num
                

print(Solution().closedIsland(
[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))

# print(Solution().closedIsland( [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))