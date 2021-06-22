class Solution:
    # 同余定理 + 前缀和 + 计数法
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum = [0]
        for i in nums:
            presum.append(presum[-1] + i)
        
        records = {0:1} #记录的是 以 前缀和 mod k 为键， 出现的次数为值的字典
        ans = 0
        for i in presum[1:]:
            # 由于 python 对于 负数取整是向负 无穷的，所以需要特殊处理
            item = i%k if i%k >= 0 else k + i%k
            if records.get(item):
                ans += records.get(item)
                records[item] += 1
            else:
                records[item] = 1
        
        return ans
