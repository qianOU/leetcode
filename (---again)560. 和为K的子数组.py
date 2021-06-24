class Solution:
    # 暴力 + 前缀和 (超时！！！！)
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = [0]
        n = len(nums)
        
        for i in nums:
            presum.append(presum[-1] + i)
        
        ans = 0
        for i in range(1, n+1):
            for j in range(i):
                if presum[i] - presum[j] == k:
                        ans += 1
        return ans     
    
    # 优化 ： 前缀和 + 前缀和 hash 表
    # 假设有 presum[i] - presum[j] = k  （j < i）
    # 则 presum[j] = presum[i] - k 也就是说以 nums[i] 为结尾的子数组如果是符合要求的
    # 则 相应的 j 的前缀和 为 presum[i] - k 出现的次数就是 以 nums[i] 为结尾的子数组符合要求的个数
    def subarraySum(self, nums: List[int], k: int) -> int:
        import collections
        ans = presum = 0
        rec = collections.defaultdict(int) # 前缀和计数表
        rec[0] = 1
        for i in nums:
            presum += i
            ans += rec[presum - k] # 找寻的 j 是小于 i 的
            rec[presum] += 1 # 最后，更新前缀和 表
        return ans