class Solution:
    # 子集背包问题
    # 二维DP问题
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target = total // 2
        n = len(nums)

        # dp[i][j] 表示 使用前 i 个数组元素，是否可以构成 和 为 j 的子集 
        # dp 数组 两个状态，即 当前到达 i 件物品决策，以及此时 子集的和大小 
        dp = [[False]*(1 + target) for i in range(1 + n)]
        # base case
        for i in range(1 + n):
            dp[i][0] = True
        
        for i in range(1, 1 + n):
            for j in range(1, 1 + target):
                # 第 i 个 数组元素，放入子集中或者不放入子集中
                dp[i][j] = dp[i-1][j] # 不放入子集
                if j >= nums[i-1] and not dp[i][j]: 
                    dp[i][j] = dp[i-1][j-nums[i-1]] # 放入子集
                
        return dp[n][target]
    
    # 空间优化：一维 DP 
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target = total // 2
        n = len(nums)

         
        dp = [False]*(1 + target) # dp[i] 表示的是 子集和 为 i 的情况是否存在
        dp[0] = True
        
        for i in range(1, 1 + n):
            for j in range(target, 0, -1):
                # 第 i 个 数组元素，放入子集中或者不放入子集中
                # dp[j] = dp[j] # 不放入子集
                if j >= nums[i-1]: 
                    dp[j] = dp[j] or dp[j-nums[i-1]] # 放入子集
                
        return dp[target]