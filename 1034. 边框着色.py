class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        check = lambda x, y: 0<=x<m and 0<=y<n
        
        cur_color = grid[r0][c0]

        visited = set([(r0, c0)])
        ans = []

        def dfs(i, j):
            flag = 0 # i,j 是否边界的表示位
            for l, r in d:
                x, y = i+l, j+r
                if check(x, y) and grid[x][y] == cur_color and (x, y) not in visited:
                    visited.add((x, y))
                    dfs(x, y)
                # 是边界的判断规则
                elif (check(x, y) and grid[x][y] != cur_color ) or (i== 0 or i == m-1 or j==0 or j == n-1):
                    flag = 1
            
            # 如果 i，j 是标识位， 则记录进列表
            if flag:
                ans.append((i, j))
        
        dfs(r0, c0)

        #更改颜色
        for i,j in ans:
            grid[i][j] = color
        
        return grid