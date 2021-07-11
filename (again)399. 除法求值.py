class Solution:
    # 方法1： 基于 有向图 + 记忆化 DFS 的方法
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict
        # relations[i][j] 表示的是 i / j 的值
        relations = defaultdict(lambda : defaultdict(int))

        for (i, j), v in zip(equations, values):
            relations[i][j] = v
            if v:
                relations[j][i] = 1/v
        
        visited = set()
        from functools import lru_cache
        @lru_cache(None)
        def dfs(cur, target):
            if cur == target:
                return 1
            
            for nex in relations[cur]:
                sign1 = cur + '-' + nex
                sign2 = nex + '-' + cur

                if  sign1 in visited or sign2 in visited:
                    continue

                visited.add(sign1)
                visited.add(sign2)
                item = dfs(nex, target)
                if item is not None:
                    return relations[cur][nex]*item

        ans = []
        for i, j in queries:
            if i not in relations or j not in relations:
                ans.append(-1.0)
            else:
                visited.clear() # 情况遍历的过程
                val = dfs(i, j)
                if val is not None:
                    ans.append(val)
                else:
                    ans.append(-1.0)
            
        return ans
    
    # 方法2： 基于 带 权重的并查集(十分有意义)
    # 根节点是分母，
    def calcEquation(self, equations, values, queries):
        class UFoid:
            def __init__(self):
                self.parents = {} # 连通性字典
                self.weight = {} # 使用的是分子做记录

            def add(self, x):
                if x not in self.parents:
                    self.parents[x] = x
                    self.weight[x] = 1
            
            # 每一步 找寻的过程，都确保 树 的深度 为 2
            # 确保了 并查集中 都是 1 步 可达 父节点的
            def find(self, x):  
                while x != self.parents[x]:
                    origin = self.parents[x]
                    self.parents[x] = self.find(origin) # 递归， 将 x 指向 x 根节点
                    self.weight[x] *= self.weight[origin]
                    x = origin

                return x
            
            # 遵循 平行四边形 规则
            def union(self, a, b, value):
                root_a, root_b = self.find(a), self.find(b)
                if root_a == root_b:
                    return 
                # 讲 b 的 分母 转换 为 a 
                self.parents[root_a] = root_b
                self.weight[root_a] = self.weight[b] * value / self.weight[a]
            
            def isconnect(self, a , b):
                root_a, root_b = self.find(a), self.find(b)
                if root_a == root_b: # 如果在同一个集合中
                    # 都转换为 同一个 分母
                    return self.weight[a] / self.weight[b]
                else:
                    return -1

        uf = UFoid()
        for (a,b),val in zip(equations,values):
            uf.add(a)
            uf.add(b)
            uf.union(a, b, val)

        
        res = [-1] * len(queries)
        for i, (a, b) in enumerate(queries):
            if a not in uf.parents or b not in uf.parents:
                res[i] = -1
            else:
                res[i] = uf.isconnect(a, b)
        
        return res
                  

print(Solution().calcEquation(
[["a","b"],["b","c"]],
[2.0,3.0],
[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
)
)