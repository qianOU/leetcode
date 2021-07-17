class Solution:
    # 暴力 从上往下递归
    def cuttingRope(self, n: int) -> int:

        from functools import lru_cache
        # n 段 切割成 m 份最大的乘积
        @lru_cache(None)
        def dfs(n, m):
            if m == 1: return n
            ans = 1
            for k in range(1, n-(m-1)+1):
                ans = max(ans, k*dfs(n-k, m-1))
            return ans
        
        res = 1
        for m in range(2, n):
            res = max(res, dfs(n, m))
        
        return res


    # 动态规划，自底向上
    def cuttingRope(self, n: int) -> int:
        if n < 4: return n - 1 # 如果绳子长度 大于等于 4 才有剪的必要
        
        dp = [0] * (n + 1) # dp[i] 表示 长度 为 i 的情况下，在 剪/不剪 的情况下能得到的乘积最大值
        # base case
        dp[1] = 1 # 表示子绳长 1 的时候不要剪最大
        dp[2] = 2 # 表示子绳长 2 的时候不要剪最大
        dp[3] = 3  # 表示子绳长 3 的时候不要剪最大

        # 之后的子绳 大于 3 都可以通过剪枝来 增加 最终 乘积
        for i in range(4, n+1):
            # 找寻切割位置, 由于切割点左右两侧是对称的，所以可以优化内循环
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        
        return dp[n]



print(Solution().cuttingRope(48))