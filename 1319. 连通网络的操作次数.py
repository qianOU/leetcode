class Solution:
    def makeConnected(self, n: int, connections) -> int:
        # 并查集
        parents = list(range(n))
        # 并查集的连通量
        count = n
        def find(x):
            while x != parents[x]:
                item = parents[x]
                parents[x] = parents[item]
                x =parents[x]
            return x
        
        def isconnect(a, b):
            return find(a) == find(b)

        def union(a, b): # 将b接在 a 上
            nonlocal count
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return 
            if root_a < root_b:
                parents[root_b] = root_a 
            else:
                parents[root_a] = root_b
            count -= 1
        
        # 初始化 parents， 判断是否有环
        net = 0
        for i, j in connections:
            # 判断是否存在环， 如果存在环的话 表示多余一条网线
            if isconnect(i, j):
                net += 1
                continue
            union(i, j)
        

        single = count
        if single > net+1: #如果 连通量的数量 大于 网线数量+1，则不可能符合题意
            return -1
        else:
            return single - 1
