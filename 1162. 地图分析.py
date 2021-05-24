class Solution:
    # 方法一：多源 BFS， 但是没有考虑 BFS 本身所具有的最短路径长度特性
    def maxDistance(self, grid) -> int:
        d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        n = len(grid)
        check = lambda x,y: 0<=x<n  and 0<=y<n 
        
        records = {}
        from collections import deque
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] and 0 in [grid[i+l][j+r] for l,r in d if check(i+l, j+r)]:
                    grid[i][j] = 2
                    q.append((i, j))

        print(q)
        count = 0
        min_ = float('-inf')
        while q:
            sz = len(q)
            for _ in range(sz):
                l,r = q.popleft()
                for i, j in d:
                    x, y = l+i, r+j
                    if check(x, y):
                        if grid[x][y] == 0 and records.get(x*n+y, 101) > count+1:
                            q.append((x, y))
                            records[x*n+y] = count + 1
                            min_ = max(min_, count+1)
    
                            
            count += 1

        return min_ if min_ != float('-inf') else -1

    # 优化：使用 多源 BFS 的特性，所以就不要 records来做记录了
    # 因为 多源 BFS， 从陆地开始搜素，每走一步，碰到的海洋都是离陆地最短距离
    def maxDistance(self, grid) -> int:
        d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        n = len(grid)
        check = lambda x,y: 0<=x<n  and 0<=y<n 
        

        from collections import deque
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] and 0 in [grid[i+l][j+r] for l,r in d if check(i+l, j+r)]:
                    q.append((i, j))

        print(q)
        count = 0
        min_ = float('-inf')
        while q:
            sz = len(q)
            for _ in range(sz):
                l,r = q.popleft()
                for i, j in d:
                    x, y = l+i, r+j
                    if check(x, y):
                        # 多源 BFS， 从陆地开始搜素，每走一步，碰到的海洋都是离陆地最短距离
                        if grid[x][y] == 0:
                            grid[x][y] = 1
                            q.append((x, y))
                            # records[x*n+y] = count + 1
                            min_ = max(min_, count+1)
    
                            
            count += 1

        return min_ if min_ != float('-inf') else -1


