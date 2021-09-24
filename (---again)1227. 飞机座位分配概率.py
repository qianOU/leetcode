class Solution:
    # 一维dp。从问题出发建立dp数组的含义
    def nthPersonGetsNthSeat(self, n: int) -> float:
        #dp[i] 表示的是有 i 位乘客的时候，第i位坐到自己座位上的概率
        # 数学推导出 dp[n] == dp[n-1] 当 n > 2 的时候
        if n == 1: return 1
        return 0.5
