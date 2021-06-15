class Solution:
    # 并查集 + 局部排序
    # 局部排序 可以进行优化， 因为题目是小写字母，所以可以使用桶排序思想，复杂度降低到 0（N）
    def smallestStringWithSwaps(self, s: str, pairs) -> str:
        # 并查集
        class Uniod:
            def __init__(self, n):
                self.parents = list(range(n))
                self.count = n
            
            def find(self, a):
                while a != self.parents[a]:
                    self.parents[a] = self.parents[self.parents[a]]
                    a = self.parents[a]
                return a
            
            def union(self, a, b):
                root_a, root_b = self.find(a), self.find(b)
                if root_a == root_b:
                    return 
                if root_a < root_b:
                    self.parents[root_b] = root_a
                else:
                    self.parents[root_a] = root_b
                
                self.count -= 1
            
            def connect(self, a, b):
                return self.find(a) == self.find(b)
        
        n = len(s)
        tmp = list(s)
        uf = Uniod(n)

        # 并查集 简历 索引之间的连通性
        for i, j in pairs:
            uf.union(i, j)
        
        import collections
        # 将同一个连通量的所有索引取出来，排序，再按原视顺序插入 tmp 数组中
        records = collections.defaultdict(list)

        for i in range(n):
            records[uf.find(i)].append(i)
        
        for item in records.values():
            
            # 使用桶排序思想优化排序过程< 降低排序的时间复杂度
            bucket = [0]*26
            for i in item:
                bucket[ord(s[i]) - ord('a')] += 1

            ans = []
            for i in range(26):
                if bucket[i]:
                    item1 = chr(ord('a') + i)
                    ans.extend([item1] * bucket[i])


            # ans = sorted(tmp[i] for i in item) # 同一分量的索引，按照字典序排序
            for j in range(len(item)): # 将排完序的插入到原视位置中
                tmp[item[j]] = ans[j]
        
        return ''.join(tmp)


print(Solution().smallestStringWithSwaps(
"dcab",
[[0,3],[1,2]]
)
)