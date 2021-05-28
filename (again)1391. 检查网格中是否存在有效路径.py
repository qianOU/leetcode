class Solution:
    # 连通性问题，可以将一个单元格 四条边剥离开，看成四个状态
    def hasValidPath(self, grid) -> bool:
        class Ufoid:
            def __init__(self, n):
                self.parents = list(range(n))
                self.count = n
            
            def find(self, a):
                while a != self.parents[a]:
                    self.parents[a] = self.parents[self.parents[a]]
                    a = self.parents[a]
                return a
            
            def connect(self, a, b):
                return self.find(a) == self.find(b)
            
            def union(self, a, b):
                r_a, r_b = self.find(a), self.find(b)
                if r_a == r_b:
                    return 
                if r_a > r_b:
                    self.parents[r_a] = r_b
                else:
                    self.parents[r_b] = r_a
                self.count -= 1
            
        
        m, n = len(grid), len(grid[0])
        check = lambda x, y: 0<=x<m and 0<=y<n
        pair = {}
        d = [(0, 1), (1, 0),(-1,0),(1,0)]
        uf = Ufoid(4*m*n)

        for i in range(m):
            for j in range(n):
                if i > 0: # 上下单元格连通
                    uf.union(i*n*4+j*4, (i-1)*n*4+j*4+1)
                if j > 0: #左右单元格连通
                    uf.union(i*n*4+j*4+2, i*n*4+(j-1)*4+3)
                # 剩下的按照道路进行连通
                if grid[i][j] == 1:
                    uf.union(i*n*4 + j*4 + 2, i*n*4 + j*4+3)
                elif grid[i][j] == 2:
                    uf.union(i*n*4 + j*4, i*n*4 + j*4+1)
                elif grid[i][j] == 3:
                    uf.union(i*n*4 + j*4+2, i*n*4 + j*4+1)
                elif grid[i][j] == 4:
                    uf.union(i*n*4 + j*4+1, i*n*4 + j*4+3)
                elif grid[i][j] == 5:
                    uf.union(i*n*4 + j*4+2, i*n*4 + j*4)
                elif grid[i][j] == 6:
                    uf.union(i*n*4 + j*4+3, i*n*4 + j*4)    

        pair = {1:(2, 3), 2:(0,1), 3:(2, 1), 4:(1,3), 5:{2, 0}, 6:{0, 3}}
        for start in pair[grid[0][0]]:
            for end in pair[grid[m-1][n-1]]:
                if uf.connect(start, m*n*4 - 4 + end):
                    return True
        
        return False

print(Solution().hasValidPath( [[1,1,2]]))
            

