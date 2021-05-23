class Solution:
    # 并查集[确定边界] + BFS【确定边界到边界的最少距离】
    def shortestBridge(self, grid: List[List[int]]) -> int:
        class Ufoid:
            def __init__(self, n):
                self.roots = list(range(n))
                self.count = n
            
            def find(self, a):
                while a != self.roots[a]:
                    item = self.roots[a]
                    self.roots[a]  = self.roots[item] # 压缩路径
                    a = self.roots[a]
                return a
            
            def connect(self, a, b):
                return find(a) == find(b)
            
            def union(self, a, b):
                root_a, root_b = self.find(a), self.find(b)
                if root_a == root_b:
                    return
                elif root_a <= root_b:
                    self.roots[root_b] = root_a
                else:
                    self.roots[root_a] = root_b
                
                self.count -= 1

        m, n = len(grid), len(grid[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        check = lambda x, y: 0<=x<m and 0<=y<n

        uf = Ufoid(m*n)
        for i in range(m):
            for j in range(n):
                if i > 0 and grid[i-1][j] == grid[i][j] == 1:
                    uf.union((i-1)*n+j, i*n+j)
                if j > 0 and grid[i][j-1] == grid[i][j] == 1:
                    uf.union(i*n+j-1, i*n+j)
        
        from collections import defaultdict
        ans = defaultdict(list)
        # 找到一个岛屿
        for i in range(m*n):
            x, y = divmod(i, n)
            # 找到边缘点
            if  grid[x][y] and 0 in [grid[x+i][y+j] for i,j in d if check(x+i, y+j)]:
                ans[uf.find(i)].append((x, y))
        
        area = list(ans.keys())
        one = area[0]
        # 另外一个岛屿边界 作为 是否到达的判断
        two  = set(ans[area[1]])

        from collections import deque
        q =   deque()
        seen = set()
        # 岛屿1的边界作为 BFS 的起点
        for i in ans[one]:
            q.append(i)
            seen.add(i)
        
        dis = -1
        
        while q:
            sz = len(q)
            for _ in range(sz):
                x, y = q.popleft()
                if (x, y) in two:
                    return dis
                for i, j in d:
                    if check(x+i, y+j) and (x+i, y+j) not in seen:
                        seen.add((x+i, y+j))
                        q.append((x+i, y+j))

            dis += 1
        return 1



