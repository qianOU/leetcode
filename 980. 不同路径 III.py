class Solution:
    def uniquePathsIII(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num = (sum(grid, []))
        total = num.count(0)
        idx = num.index(1)
        x, y = divmod(idx, n)

        from functools import lru_cache
        # @lru_cache(None)
        count = 0
        def dfs(i, j, total):
            nonlocal count
            for l, r in d:
                x, y = i+l, j+r
                if 0<=x<m and 0<=y<n and grid[x][y]!=-1:
                    if grid[x][y] == 2 and not total:
                        count += 1
                        return 

                    if not grid[x][y]:
                        grid[x][y] = -1
                        dfs(x, y, total-1)
                        grid[x][y] = 0
            


        print(x,y, total)
        grid[x][y] = -1
        dfs(x, y, total)
        return  count

print(Solution().uniquePathsIII([[0,1],[2,0]]))