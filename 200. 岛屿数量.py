class Solution:
    # 思路 1 使用 set 保存走过的路径
    # 思路二是 使用 DFS 将走过 的陆地 置为 0，由此只需要计数  1（首次探索的陆地）的个数 即可 

    def numIslands(self, grid) -> int:
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        check = lambda x, y: 0<=x<m and 0<=y<n
        visited = set()

        def dfs(i, j):
            count = 0
            for l, r in d:
                x, y =i+l, j+r
                if check(x, y) and (x, y) not in visited and grid[x][y]=='1':
                    visited.add((x, y))
                    if not dfs(x, y):
                        return 
                    count += 1
                elif (x, y) in visited or not check(x, y) or  grid[x][y]=='0':
                    count += 1
            
            if count == 4:
                return True
            

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (i, j) not in visited:
                    visited.add((i, j))
                    if dfs(i, j):
                        count += 1
        
        return count
    