class Solution:
    # 先排序 + 整除关系的传导性 --> 类时于 LIS 的 dp 问题
    # 本体一大特点是 需要 找到 最大整数集合，而不是单纯的 集合大小
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        # dp的状态标记就是 索引 i
        dp = [1]*n # dp[i] 表示的是 以 nums[i] 为最大元素的最大集合的大小
        # g[i] = j 表示的就是 dp[i] = dp[j] + 1
        g  = [0]*n # g[i] 表示的是 状态转移的过程， 

        for i in range(n):
            # 我们要将 nums[i] 接到 i 之前 的 最大集合 j 且满足， nums[i] % nums[j] == 0
            length, prev = 1, i  # 默认 以 nums[i] 作为最大集合首元素, prev 记录 从 哪个状态转移到 i
            for j in range(i): 
                if nums[i] % nums[j] == 0 and dp[j] + 1 > length:
                    length = dp[j] + 1
                    prev = j # 表示 从 j 转移到 i
            
            dp[i] = length
            g[i] = prev

        # 遍历找寻最大长度的 集合， 以及 索引位置，方便你后序进行逆向回溯
        length = 0
        idx = 0
        for i in range(n):
            if dp[i] > length:
                idx = i
                length = dp[i]

        # 进行状态回溯,从最大元素的索引进行回溯
        ans = []
        prev = None
        while idx != prev:
            ans.append(nums[idx])
            prev = idx
            idx = g[prev]
        
        return ans[::-1]


