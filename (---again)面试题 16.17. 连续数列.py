class Solution:
    # 动态规划
    def maxSubArray(self, nums) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)
    
    # 分治
    # 保持一个区间的四个有关状态！ 妙！
    def maxSubArray(self, nums) -> int:
        
        # answer : [lsum, rsum, msum, isum]
        # lsum 表示 [l, r] 内以 l 为左端点的最大子段和
        # rsum 表示 [l, r] 内以 r 为右端点的最大子段和
        # msum 表示 [l, r] 内最大的 子段和
        # isum 表示 [l, r] 内区间和
        def get_answer(left, right):
            if right == left:
                return [nums[left]]*4
            
            mid = left + (right - left) // 2
            l1 = get_answer(left, mid)

            r1 = get_answer(mid + 1, right)
            return [
                max(l1[0], l1[-1] + r1[0])
                ,max(r1[1], r1[-1] + l1[1])
                ,max(l1[2], r1[2], l1[1] + r1[0])
                ,l1[-1] + r1[-1]
                
            ]
        
        return get_answer(0, len(nums)-1)[2]

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))