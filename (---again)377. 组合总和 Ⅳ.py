class Solution:

    # 方法1： 递归做法 记忆化 备忘录
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort() # 排序
   
        # 二分查找 第一个 大于 cum 的元素
        def bin_search(cum):
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > cum:
                    r = mid - 1
                else:
                    l = mid + 1
            return l


        n = len(nums)

        @functools.lru_cache(None)
        def dfs(cum):
            #和为 cum 的 组合有多少个
            ans = 0
            if cum == 0:
                return 1

            # 二分查找 第一个 大于 cum 的元素
            idx =  bin_search(cum)

            for i in range(idx):
               ans += dfs(cum - nums[i])

            return ans
        
        return dfs(target)

    # 方法2： 动态规划 (有点类似完全背包问题， 物品可以重复选择问题)
    # 但是状态定义不同
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        length = target # 组合的最大长度

        # dp[i][j] 表示的是 当组合的长度为 i 的时候， 和为 j 的情况下的方案数， 也就是排列数
        dp = [[0]*(target+1) for i in range(1+length) ]
        
        # base - case
        dp[0][0] = 1
        
        for i in range(1, 1+length):
            for j in range(1, 1+target):
                for num in nums:
                    if j >= num:
                        dp[i][j] += dp[i-1][j-num]

        return sum(dp[i][target] for i in range(1+length))
    
    # 一维 DP
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1) # dp[i] 表示的是 和为 i 的方案数
        # b-c
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num] # 以 num 组合的作为结尾
        return dp[target]