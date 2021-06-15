class Solution:
    def countServers(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        rows = []
        cols = []
        ans = 0
        for i in range(m):
            item = sum(grid[i])
            if item > 1:
                ans += item
                rows.append(i)
        
        for i in range(n):
            item = sum(grid[j][i] for j in range(m))
            if item > 1:
                ans += item
                cols.append(i)
                
        
        print(rows, cols)
        for r in rows:
            for c in cols:
                if grid[r][c]:
                    ans -= 1
        
        return ans


print(Solution().countServers([[1,0],[1,1]]))