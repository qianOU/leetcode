class Solution:
    # 方法一： 暴力模拟法 超时失败
    def minimumHammingDistance(self, source, target, allowedSwaps) -> int:
        
        n = len(source)
        hingtong = n
        visited = set()
        visited.add(tuple(source))

        def dfs(cur):
            nonlocal hingtong

            hingtong = min(hingtong, sum(1 if cur[i]!=target[i] else 0 for i in range(n)))
            
            
            swap_times = 0
            tmp = cur.copy()
            for i, j in allowedSwaps:
                cur = tmp
                cur[i], cur[j] = cur[j], cur[i]
                if tuple(cur) not in visited:
                    visited.add(tuple(cur))
                    swap_times += 1
                    dfs(cur)
        

        
        dfs(source)

        return hingtong
    
    # 思路2： 并查集 因为 [0, 1] , [1, 2] 也九表示 0，1，2 在一个连通量上，可以得到三者的任意组合
    # 因此 转换问题就是求 不同连通量上的 索引， source 和 target 不同元素的个数之和
    def minimumHammingDistance(self, source, target, allowedSwaps) -> int:

        class Ufoid:
            def __init__(self, n):
                self.parents = list(range(n))
                self.count = n

            
            def find(self, a):
                while a != self.parents[a]:
                    self.parents[a] = self.parents[self.parents[a]]
                    a = self.parents[a]
                
                return a
            
            def union(self, a, b):
                root_a , root_b = self.find(a), self.find(b)
                if root_a == root_b:
                    return
                if root_a < root_b:
                    self.parents[root_b] = root_a
                else:
                    self.parents[root_a] = root_b
                
                self.count -= 1
            
        n = len(target)
        uf = Ufoid(n)
        
        # 搭建连通性
        for i, j in allowedSwaps:
            uf.union(i, j)

        from collections import defaultdict
        dic = defaultdict(list)
        # 构建字典，连通量根节点 ---> 连通量内部所有索引列表  
        for i in range(n):
            root = uf.find(i)
            dic[root].append(i)
        
        from collections import Counter
        ans = 0
        # 逐个比较不同连通量直接，存在的不同字符的数量
        for k, v in dic.items():
            a = Counter(source[i] for i in v)
            b = Counter(target[i] for i in v)
            # 注意：需要对 不同字符的计数次数做加和
            ans += sum((b - a).values()) 
        
        return ans


print(Solution().minimumHammingDistance([32,18,60,3,8,25,85,68,40,91,53,46,29,35,25,72,13],
[32,3,6,12,68,19,59,52,74,91,67,30,12,92,78,72,96],
[[6,9],[7,12],[7,0],[10,0],[7,3],[2,5],[11,1],[8,5],[6,7],[10,6],[0,4],[15,8],[4,10],[2,6],[9,14],[11,5],[5,4],[13,10],[4,16],[9,16],[15,14],[16,14],[0,1],[12,3],[12,1],[8,12],[4,15],[11,2],[14,5],[10,14],[13,6],[11,15],[8,7],[16,6],[11,16],[14,0],[3,11],[15,1],[9,8],[4,12],[2,12],[6,14],[15,7],[12,13],[1,16],[16,13],[5,1],[0,11],[6,3],[10,1],[11,6],[0,5],[8,0],[4,11],[5,3],[7,2],[9,13],[10,5],[6,4],[16,15],[7,5],[0,2],[3,15],[1,3],[13,8],[8,4],[2,8],[5,13],[15,10],[14,11],[7,11],[15,0],[10,3],[1,14],[10,8],[4,13],[13,2],[11,9],[3,16],[16,8],[6,15],[13,11],[7,14],[14,12],[13,15],[1,4],[12,0],[9,3],[3,2],[1,9],[2,14],[8,6],[5,16],[16,10],[13,7],[6,0],[7,1],[9,0],[4,3],[4,2],[12,9],[5,9],[4,7],[11,10],[6,5],[0,16],[16,7],[12,16],[0,3],[3,14],[2,1],[8,14],[9,4],[9,2],[9,15],[5,12],[12,10],[10,7],[2,16],[13,3],[1,13],[8,11],[4,14],[10,2],[10,9],[5,15],[6,12],[11,12],[7,9],[15,12],[13,14],[13,0],[8,3],[1,8],[2,15]]))