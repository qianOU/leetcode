class Solution:
    def orangesRotting(self, grid) -> int:
        d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m, n = len(grid), len(grid[0])
        check = lambda x, y: 0<=x<m and 0<=y<n
        fresh = 0


        from collections import deque
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        # 如果没有新鲜橘子， 直接返回 0 
        if not fresh:
            return 0

        count = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                l, r  = q.popleft()
                for i, j in d:
                    x, y = l+i, r+j
                    if check(x, y) and grid[x][y] == 1:
                        fresh -= 1
                        grid[x][y] = 2
                        q.append((x, y))
            count += 1
        
        return count - 1 if not fresh else -1


print(Solution().orangesRotting([[0]]))