class Solution:
    # 思路1：超时，动态规划设计的不合理
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        m = k + maxPts
        # dp[i][j] 表示当前分数是 i 的时候,最后的选择是 j 的概率
        dp = [[0]*(1+maxPts) for i in range(1+m)]
        p = 1 / maxPts
        # base case
        dp[0][0] = 1

        c, thr = 0, int(math.log(10**6, maxPts)) + 2 # 最大转移步数
        for i in range(1, 1+m):
            if c > thr: break
            for j in range(1, 1+maxPts):
                if 0 <= i - j < k:
                    dp[i][j] += p * sum(dp[i-j]) 
            c += 1
        return sum(sum(dp[i]) for i in range(k, n+1))
    
    # 思路2: 重新设计转态转移过程
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0]*(maxPts + k) # dp[i] 表示从 i 积分开始进行游戏获胜的概率
        # 结束后在[k, n] 的范围内获胜的概率为 1
        for i in range(k, min(n, maxPts + k - 1) + 1 ): dp[i] = 1
        # base case
        dp[k-1] = min(n - k + 1, maxPts) / maxPts

        for i in range(k-2, -1, -1):
            dp[i] = dp[i+1] + (dp[i+1] - dp[i+maxPts+1]) / maxPts  # 从相邻元素的差来寻求转态转移方程
        
        return dp[0]