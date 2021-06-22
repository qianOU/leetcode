class Solution:
    # 思路1： 二维 DP 
    def maxProduct(self, nums) -> int:
        n = len(nums)
        # dp[i][j] 表示的是当 以 i 位置为结尾元素 时，乘积是 j 状态的情况下（j指的是乘积为正数（状态0）或者负数（状态1）），的最大乘积数
        dp = [[0,0] for i in range(n)]
        dp[0] = [max(nums[0], 0), min(nums[0], 0)]
        pos = False # 记录是否出现大于 0 的元素，为了缩短运行时间，减少比较的次数
        ans = nums[0] #
        for i in range(1, n):
            if nums[i] > 0: # 如果当前元素，为正数更新 dp[i][j]
                dp[i][0] = max(nums[i], dp[i-1][0]*nums[i])
                dp[i][1] = min(dp[i-1][1]*nums[i], 0)
            elif nums[i] < 0:# 如果当前元素，为负数数更新 dp[i][j]
                dp[i][0] = max( dp[i-1][1]*nums[i], 0)
                dp[i][1] = min(dp[i-1][0]*nums[i], nums[i])
            else: # 如果当前元素是 0 的话，dp[i][j] = 0
                ans = max(ans, 0)
                
            if dp[i][0]: # 更新 ans
                ans = max(ans, dp[i][0])
                pos = True
            if not pos and dp[i][1]: # 更新负数解的时候是当前仅当 无正数结果的时候，已级存在负数乘积的时候
                ans = max(ans, dp[i][1])

        
        return ans 

    # 思路2： 一维 DP 
    def maxProduct(self, nums) -> int:
        n = len(nums)
        dp_min = [1]*(n+1) # 以 nums[i-1]为结尾元素的乘积最小值
        dp_max = [1]*(n+1)  # 以 nums[i-1]为结尾元素的乘积最大值

        ans = nums[0]
        for i in range(n):
            dp_min[i+1] = min(dp_max[i]*nums[i], dp_min[i]*nums[i], nums[i])
            dp_max[i+1] = max(dp_max[i]*nums[i], dp_min[i]*nums[i], nums[i])
            ans = max(ans, dp_min[i+1], dp_max[i+1])
        
        return ans