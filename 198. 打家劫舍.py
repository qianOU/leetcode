class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        n = len(nums)

        # dp[i] 表示在 第i家的时候，能获得的最大金额
        dp = [0]*(n+1)
        dp[1] = nums[0]

        for i in range(2, n+1):
            dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
        
        return dp[n]

print(Solution().rob([2,7,9,3,1]))