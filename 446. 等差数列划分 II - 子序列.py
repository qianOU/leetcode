class Solution:
    # 动态规划
    def numberOfArithmeticSlices(self, nums) -> int:
        from collections import defaultdict

        n, ans = len(nums), 0
        record = defaultdict(int) # 记录公差的记录表
        dp = [defaultdict(int) for i in range(n)]
        for i in range(n):
            for j in range(i):
                ans += dp[j][nums[i] - nums[j]]
                dp[i][nums[i] - nums[j]] += dp[j][nums[i] - nums[j]] + 1
      
        return ans

print(Solution().numberOfArithmeticSlices([2, 4, 6, 8, 10]))