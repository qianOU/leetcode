class Solution:
    # 同一个连通分量的一定 可以 删除到只剩 一个
    def removeStones(self, stones) -> int:
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
        
        n = len(stones)
        uf = Ufoid(n)

        # 使用集合 时间复杂度 下降为 O（n）
        # 记录 行坐标到 stones 索引的映射关系
        rows = {}
        # 记录 列坐标到 stones 索引的映射关系
        cols = {}
        for idx, (i, j) in enumerate(stones):
            if i in rows:
                uf.union(idx, rows[i])
            rows[i] = idx # 跟新坐标 对应 的索引

            if j in cols:
                uf.union(idx, cols[j])
            cols[j] = idx
        

        # 最原视的 0（n**2） 的 判断节点连通性
        # for i in range(n):
        #     r, c = stones[i]
        #     for j in range(i+1, n):
        #         if stones[j][0] == r:
        #             uf.union(i, j)
        #         elif stones[j][-1] == c:
        #             uf.union(i, j)
        
        

        return n - uf.count

        