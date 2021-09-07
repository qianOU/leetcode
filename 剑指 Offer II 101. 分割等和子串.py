import  pprint
class Solution:
    def canPartition(self, nums) -> bool:
        total = sum(nums)
        n = len(nums)
        if total & 1: return False
        target = total >> 1
        dp = [[False]*(1+target) for i in range(1+n)]
        # base case
        for i in range(1+n): dp[i][0] = True
        for i in range(1, 1+n):
            for j in range(1, 1+target):
                dp[i][j] = dp[i-1][j]
                if j - nums[i-1] >= 0:
                    dp[i][j] |= dp[i-1][j-nums[i-1]] # 只要有一个满足即可
            if dp[i][target]: return True

        return False

print(Solution().canPartition([14,9,8,4,3,2]))