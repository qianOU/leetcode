class Solution:
    # 动态规划
    def maxSumDivThree(self, nums: List[int]) -> int:
        n =  len(nums)
        # dp[i][j] 表示的是在[0， i) 区间范围内，总和余 3 为 j 的状态下的最大和问题
        dp = [[0, float('-inf'), float('-inf')] for i in range(1+n)]
        for i in range(n):
            a = nums[i] % 3
            for j in range(3):
                dp[i+1][j] = max(dp[i][j], nums[i] + dp[i][(j - a) % 3])
        
        return dp[-1][0]