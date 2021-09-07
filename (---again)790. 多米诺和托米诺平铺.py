class Solution:
    # 思路1： 动态规划
    def numTilings(self, n: int) -> int:
        base = 10**9 + 7
        # 每一列可以用四个状态标识，分别是指 0-1行都空，0行空，1行空，0-1行都不空
        dp = [[0]*4 for i in range(n)]
        # base case
        dp[0] = [1, 0, 0, 1] # base case 当只有一行的时候，只能竖着铺，或者不铺设两个状态
        for i in range(1, n):
            dp[i][0] = dp[i-1][3]
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % base
            dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % base
            dp[i][3] = (dp[i-1][0] + dp[i-1][3] + dp[i-1][1] + dp[i-1][2]) % base

        return dp[n-1][3]
    
    # 思路2： 动态规划，有转移矩阵，因此可以使用矩阵快速幂运算
    def numTilings(self, n: int) -> int:
        base = 10**9 + 7
        P = [[0, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 1, 1, 1]] # 状态转移矩阵
        def mat_mul(a, b):
            m, k, n = len(a), len(a[0]), len(b[0])
            ans = [[0]*n for i in range(m)]
            for i in range(m):
                for j in range(n):
                    ans[i][j] = sum(a[i][k1]*b[k1][j] for k1 in range(k)) % base
            return ans

        # 快速幂
        ans = [[1], [0], [0], [1]]
        n -= 1
        while n:
            if n & 1:
                ans = mat_mul(P, ans)
            n >>= 1
            P = mat_mul(P, P)
        return ans[-1][0]
        