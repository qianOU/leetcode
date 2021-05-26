class Solution:
    # 方法一 : DFS
    def findTargetSumWays(self, nums, target: int) -> int:
        n = len(nums)
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, total):
            if i==n:
                return int(total == target)
            return dfs(i+1, total + nums[i]) + dfs(i+1, total-nums[i])
        
        return dfs(0,0)
    
    # 方法2： 动态规划  背包问题
    def findTargetSumWays(self, nums, target: int) -> int:
        n = len(nums)
        if  (target + sum(nums))%2 or target > sum(nums):
            return 0

        pos = (target + sum(nums)) // 2

        # dp[i][j] 表示使用 nums前 i 个元素，恰好可以组合成 j 的组合数
        dp = [[0]*(pos+1) for _ in range(n+1)] 

        # base case
        # dp[0][...] = 0
        # 注意 传统的 dp[...][0] = 1 表示背包容量为0，只有一种情况， 无为而知
        # 在此处不成立，因为 为 物品元素也可能为0， 所以情况数不一定为 1
        dp[0][0] = 1
        
        for i in range(1, n+1):
            for j in range(0, pos+1):
                # 两种选择，放或者不放入书包
                if j-nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    # 空间不够，只能不放入物品 num[i-1]， 注意num索引是从0开始的
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][pos]


print(Solution().findTargetSumWays(
[1,1,1,1,1],
3
))