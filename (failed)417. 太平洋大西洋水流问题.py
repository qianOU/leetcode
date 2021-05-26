class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
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
                return self.find(a) ==  self.find(b)
            
            def union(self, a, b):
                root_a, root_b = self.find(a), self.find(b)
                if root_a < root_b:
                    self.parents[root_b] = root_a
                else:
                    self.parents[root_a] = root_b
                
                self.count -= 1
            
        
        m, n = len(heights), len(heights[0])
        uf = Ufoid(m*n+1)

        for i in range(m-1):
            uf.union(i*n, 0)
            uf.union(i*n+n-1, m*n-1)
        
        for j in range(n-1):
            uf.union(j, 0)
            uf.union((m-1)*n+j, m*n-1)
        uf.union(a, b)
        from collections import deque

        
        