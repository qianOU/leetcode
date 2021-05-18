class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        check = lambda x, y: 0<=x<m and 0<=y<n

        visited = set([0, 0])

        def dfs(i, j):
            if not check(i, j):
                return 0
            
            for l, r in d:
                if check(i)
            