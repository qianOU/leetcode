class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
       
        d = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        n = len(grid)
        check = lambda x,y: 0<=x<n and 0<=y<n

        if grid[0][0] or grid[n-1][n-1]:
             return -1

        from collections import deque
        q = deque()
        visited = set([(0,0)])
        q.append((0, 0))

        count = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                l, r = q.popleft()
                if l == n-1 and r==n-1:
                    return count+1
                
                for i, j in d:
                    x, y = i+l, j+r
                    if (x, y) not in visited and check(x, y) and not grid[x][y]:
                        visited.add((x, y))
                        q.append((x, y))
                
            count += 1
        
        return -1