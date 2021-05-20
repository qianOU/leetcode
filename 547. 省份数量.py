class Solution:
    # 方法一： 并查集
    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected)
        # 并查集
        parents = list(range(n))
        count = n # 记录连通量， 每次 union 不同组时，减一
        def find(x):
            while x != parents[x]:
                item = parents[x]
                parents[x] = parents[item]
                x =parents[x]
            return x
        
        def isconnect(a, b):
            return find(a) == find(b)

        # 将b接在 a 上, find(a)
        def union(a, b): 
            nonlocal count
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return 
            parents[root_b] = root_a 
            count -= 1
        
        # 初始化 parents 注意不是对称矩阵
        for i in range(n):
            for j in range(i, n): 
                if isConnected[i][j]:
                    union(i, j)
                   
        # return len(set(parents)) #不能用 根节点的数目进行判断连通量，因为 并查集其实具有和树一样的层次结构
        return count

    # 方法二： DFS
    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected)
        # 构建邻接表
        count = 0
        visited = set() # 记录已经走过的 节点, 实际就是所有的已知省份集合
        def dfs(i):
            visited.add(i)
            for j in range( n):
                if  j not in visited and isConnected[i][j]:
                    dfs(j)

            visited.add(i)
        for i in range(n):
            if i not in visited: # 如果 i 不在已知的省份中， 搜索包含 i 的省份
                dfs(i)
                count += 1

        return count