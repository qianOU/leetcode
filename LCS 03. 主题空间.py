from typing import List

class Solution:
    def largestArea(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        grid = [list(i) for i in grid]
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans = 0

        def dfs(x, y, kind):
            if x in (0, m-1) or y in (0, n-1): return float('-inf')
            grid[x][y] = None
            ans = 0            
            for i, j in d:
                x1, y1 = x+i, y+j
                if 0 <= x1 < m and 0 <= y1 < n:
                    if grid[x1][y1] == '0':  ans += float('-inf')
                    elif grid[x1][y1] == kind:
                        ans += dfs(x1, y1, kind)
            return ans + 1
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] and grid[x][y] != '0':
                    ans = max(dfs(x, y, grid[x][y]), ans)
        
        return ans


print(Solution().largestArea(["11111100000","21243101111","21224101221","11111101111"]))