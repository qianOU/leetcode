n = 9
w = [88, 68, 80, 29, 35, 17, 68, 25, 74]
num = [7, 2, 1, 6, 5, 4, 9, 8, 3]
ans = [0]*n
# 删除比较难考虑，考虑从后往前的构建过程
# 连通性问题

from collections import defaultdict

class Ufoid:
    def __init__(self, weight):
        n = len(weight)
        self.root = list(range(1+n))
        self.count = n
        self.weight = dict(zip(range(1, 1+n), weight))
        self.ans = 0
    
    def find(self, a):
        while a != self.root[a]:
            tmp = self.root[a]
            self.root[a] = self.root[self.root[a]]
            a = tmp
        return a

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        if self.connected(a, b): 
            self.ans = max(self.ans, self.weight[a], self.weight[b])
            return
        root_a, root_b = self.find(a), self.find(b)
        if root_a < root_b:
            self.root[root_b] = root_a
            self.weight[root_a] += self.weight[root_b]
            self.ans = max(self.ans, self.weight[root_a])
        else:
            self.root[root_a] = root_b 
            self.weight[root_b] += self.weight[root_a]
            self.ans = max(self.ans, self.weight[root_b])
    

uf = Ufoid(w)
has_done = set()
for i in range(n, 0, -1):
    ans[i-1] = uf.ans
    has_done.add(num[i-1])
    uf.union(num[i-1], num[i-1])
    for p in [-1, 1]:
        if num[i-1] + p in has_done:
            uf.union(num[i-1], num[i-1] + p)


for i in ans:
    print(i)
            
        


