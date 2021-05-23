class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
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
                root_a, root_b = self.find(a), self.find(b)
                if root_a == root_b:
                    return
                if root_b < root_a:
                    self.parents[root_a] = root_b
                else:
                    self.parents[root_b] = root_a
                
                self.count -= 1
            
        
        