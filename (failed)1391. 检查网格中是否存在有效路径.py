class Solution:
    def hasValidPath(self, grid) -> bool:
        class Ufoid:
            def __init__(self, n):
                self.parents = list(range(n))
                self.count = n
            
            def find(self, a):
                while a != self.parents[a]:
                    self.parents[a] = self.parents[self.parents[a]]
                    a = self.parents
                return a
            
            def connect(self, a, b):
                return self.find(a) == self.find(b)
            
            def union(self, a, b):
                r_a, r_b = self.find(a), self.find(b)
                if r_a == r_b:
                    return 
                if r_a > r_b:
                    self.parents[r_a] = r_b
                self.parents[r_b] = r_a
                self.count -= 1
            
        
        m, n = len(grid), len(grid[0])
        check = lambda x, y: 0<=x<m and 0<=y<n
        pair = {1:{1,5,3}, 2:{4,2,6},3:{2,6}, 4:{1,5,3}, 5:{2,4}, 6:{1,3,5}}
        d = [(0, 1), (1, 0),(-1,0),(1,0)]
        uf = Ufoid(m*n)

        from collections import deque
        q = deque()
        q.append((0, 0))
        visited = set([(0, 0)])

        while q:
            x, y = q.popleft()
            print(x, y)
            if x == m-1 and y==n-1:
                return True
            
            for i,j in d:
                l, r =  x+i, y+j
                if check(l, r) and grid[l][r] not in visited and grid[l][r] in pair[grid[x][y]]:
                    visited.add((l, r))
                    # uf.union(x*n+y, l*n+r)
                    q.append((l, r))
                    break

        return False  

print(Solution().hasValidPath( [[1,2,1],[1,2,1]]))
            

