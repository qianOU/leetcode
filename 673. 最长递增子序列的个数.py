class Solution:
    # LIS 0(n^2)
    # TODO: 应该有更优的解法
    def findNumberOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [[1, 1]]*n # dp[i] 表示的是 以 nums[i] 为结尾的LIS长度以及相应的方案数
        ans = 1
        # base case 
        for i in range(1, n):
            for j in range(i):      
                if nums[j] < nums[i]:
                    item = dp[j][0] + 1
                    if item > dp[i][0]:
                        dp[i] = [item, dp[j][1]]
                    elif item == dp[i][0]: dp[i][1] += dp[j][1]
            ans = max(ans, dp[i][0])

        return sum(dp[i][1] for i in range(n) if dp[i][0] == ans)
    

print(Solution().findNumberOfLIS([3,1,2]))