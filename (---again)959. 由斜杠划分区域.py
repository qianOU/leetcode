class Solution:
    # 思路一：
    # 构建图矩阵， 转换为 岛屿问题
    # 小细节是 原矩阵的每条边要划分成 起点 中点 终点三部分， 细节方面 ： 两条边不要有公用点
    def regionsBySlashes(self, grid) -> int:
        n = len(grid)
        # 构建 矩阵
        dp = [[0]*(3*n) for i in range(3*n)]
        
        # 转换矩阵
        i = 0
        while i< 3*n:
            j = 0
            while  j< 3*n:
                # grid 中 1个元素对应着 三个点
                if grid[i//3][j//3] == '\\':
                    dp[i][j] = 1
                    dp[i+1][j+1] = 1
                    dp[i+2][j+2] = 1
                elif grid[i//3][j//3] == '/':
                    dp[i][j+2] = 1
                    dp[i+1][j+1] = 1
                    dp[i+2][j] = 1
                j += 3
            i += 3

        # print(dp)

        check = lambda x, y: 0<=x<3*n and 0<=y<3*n
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # 主要是 考察 连通的 0 的数量
        def dfs(i, j):
            for l, r in d:
                x, y = i+l, j+r
                if check(x, y) and (x, y) not in visited and not dp[x][y]:
                    visited.add((x, y))
                    dfs(x, y)
        
        count = 0
        visited = set()
        for i in range(3*n):
            for j in range(3*n):
                if not dp[i][j] and (i, j) not in visited:
                    visited.add((i, j))
                    dfs(i, j)
                    count += 1
        
        return count
    
    # 思路2 ： 并查集
    def regionsBySlashes(self, grid) -> int:
        n = len(grid)

        class Ufoid:
            def __init__(self, n):
                self.roots = list(range(n*n*4))
                self.count = n*n*4
            
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
        
        # 找到 r,c 单元格 位置，并且 i 是单元格内部编号 0-3 
        def get_pos(r, c, i):
            return (r*n + c)*4 + i
        
        uf = Ufoid(n)

        for r in range(n):
            for c in range(n):
                if  r > 0: # 向下合并的过程
                    uf.union(get_pos(r-1, c, 0), get_pos(r, c, 2))
                if c > 0:
                    uf.union(get_pos(r, c-1, 1), get_pos(r, c, 3))
                if grid[r][c] == '\\':
                    uf.union(get_pos(r, c, 3), get_pos(r, c, 0))
                    uf.union(get_pos(r, c, 2), get_pos(r, c, 1))
                elif grid[r][c] == '/':
                    uf.union(get_pos(r, c, 3), get_pos(r, c, 2))
                    uf.union(get_pos(r, c, 1), get_pos(r, c, 0))
                elif grid[r][c] == ' ':
                    uf.union(get_pos(r, c, 0), get_pos(r, c, 1))
                    uf.union(get_pos(r, c, 0), get_pos(r, c, 2))
                    uf.union(get_pos(r, c, 0), get_pos(r, c, 3))

        return uf.count
