class Solution:
    # 十分巧妙
    # tips 1: 因为每次分出去的量都是25的倍数，因此可以 n/25 缩小规模
    # tips 2: 题目只是要求 10-6 的精度，因此存在一个阈值，当 n > thr 的时候可以截断
    def soupServings(self, n: int) -> float:
        if n > 4800: return 1 # 极限
        n = (n + 24) // 25  # 向上整除25来缩小规模
        # dp[i][j] 表示的是 当 A余 i 毫升， B余 j 毫升时，A先分完的概率 + A和B同时分配的概率/2
        dp = [[0]*(n+1) for j in range(n+1)]
        # base case
        dp[0][0] = 0.5 # 同时分配完的概率
        for i in range(1, 1+n):
            dp[0][i] = 1 # A 先分完

        for i in range(1, 1+n):
            for j in range(1, 1+n):
                dp[i][j] = 0.25*(dp[max(i-4, 0)][j] + dp[max(i-3, 0)][j-1] + dp[max(i-2, 0)][max(j-2, 0)] + dp[i-1][max(j-3, 0)])

        return dp[n][n]

print(Solution().soupServings(4801))