class Solution:
    # 暴力 超时
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [0] * (n+1) # 前n项和
        for i in range(1, n+1):
            presum[i] = presum[i-1]  + nums[i-1]
        
        max_ = 0
        for i in range(n-1):
            min_ = nums[i]
            for j in range(i, n):
                min_ = min(min_, nums[j])
                max_ = max(min_*(presum[j+1]-presum[i]), max_)

        return max_


        def maxSumMinProduct(self, nums: List[int]) -> int:
            n = len(nums)
            presum = [0] * (n+1) # 前n项和
            for i in range(1, n+1):
                presum[i] = presum[i-1]  + nums[i-1]
            
