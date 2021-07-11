class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        if n % 2 == 0: # 如果是偶数先手必胜
            return  True
        else: # 如果是奇数的情况
            # 动态规划
            # dp[i][j] 表示的是当前玩家 在[i，j] 区间内能获得的最大分差
            dp = [[0]*n for i in range(n)]
            # base - case 
            # for any i > j, dp[i][j] = 0
            for i in range(n):
                dp[i][i] = nums[i]
            
            for i in range(n-1, -1, -1):
                for j in range(i+1, n):
                    # 做选择，最大化当前的分差
                    dp[i][j] = max(
                        # 由于玩家都是理性人，因此其会在[i+1， j]区间最大化其分差
                        nums[i] - dp[i+1][j], # 表示当前玩家在拿 nums[i] 的时候，能获得的最大分差
                        nums[j] - dp[i][j-1]
                    )

            return dp[0][n-1] >= 0
