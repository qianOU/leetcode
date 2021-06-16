class Solution:
    # 暴力解法， 效率极低！！！ 
    # 元素入集合操作还是挺费时的
    def tupleSameProduct(self, nums: List[int]) -> int:
        import collections
        rec = collections.defaultdict(set)

        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                rec[nums[i]*nums[j]].add(frozenset([nums[i], nums[j]]))
    
        ans = 0
        for i in rec:
            n = len(rec[i])
            if n >= 2:
                ans += (n-1)*n//2*8
        
        return ans

    # 优化：其只需要知道有多少排列，不需要知道具体的排列样式，所以只需要对于 乘积 进行计数即可
    def tupleSameProduct(self, nums: List[int]) -> int:
        import collections
        rec = collections.defaultdict(int)

        n = len(nums)
        for i in range(n):
            # j 从 i+1， 开始遍历 因为元素都是不重复的，就确保了 不存在 (nums[i], nums[j]) 的重复出现
            for j in range(i+1, n):
                rec[nums[i]*nums[j]] += 1
    
        ans = 0
        for i in rec:
            n = rec[i]
            if n >= 2:
                ans += (n-1)*n//2*8
        
        return ans
