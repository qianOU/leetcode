class Solution:
    # 思路一：朴素思想 排序 + 单指针遍历
    # 思路二： hash 表
    def longestConsecutive(self, nums: List[int]) -> int:
        set_a = set(nums)
        max_len = 0

        for i in set_a:
            if i-1 not in set_a: #只以 最小值作为 搜索的起始节点
                cur_num = i
                cur_len = 1

                while 1 + cur_num in set_a:
                    cur_num += 1
                    cur_len += 1
                
                max_len = max(max_len, cur_len)
        
        return max_len


    # 思路三： 并查集
    def longestConsecutive(self, nums: List[int]) -> int:
        class Ufoid:
            import collections
            
            def __init__(self, nums):
                # 因为nums中的数字范围巨大，不适宜使用 大数组
                self.parents = {n: n for n in nums} 
                self.counts = collections.defaultdict(lambda : 1)

            
            def find(self, a):
                while a != self.parents[a]:
                    self.parents[a] = self.parents[self.parents[a]]
                    a = self.parents[a]
                return a
            
            # b > a
            def union(self, a, b):
                root_a, root_b = self.find(a), self.find(b)
                if root_a == root_b:
                    return
                self.parents[root_b] = root_a
                # 子树合并，结点数相加
                self.counts[root_a] += self.counts[root_b]
            
        
        ufoid = Ufoid(nums)
        for i in nums:
            if i-1 in ufoid.parents:
                ufoid.union(i-1, i)
        
        return max(ufoid.counts.values())
    
    # 动态规划

    def longestConsecutive(self, nums: List[int]) -> int:
        # 形式 dp 数组的功能，
        # dp[i]记录的是 以 i 为端点的，最长连续序列长度
        record = {}
        ans = 0

        for i in nums:
            # 如果是未被遍历过的节点
            if i not in record:
                # i-1 作为边界的时候，其最长连续序列长度
                left = record.get(i-1, 0)
                # i+1 作为边界的时候，其最长连续序列长度
                right = record.get(i+1, 0)

                record[i] = 1 # 遍历过 i 置为 1

                cur_len = left + 1 + right
                ans = max(ans, cur_len)

                # 更新新端点状态
                record[i - left] = cur_len
                record[i + right] = cur_len
        
        return ans

