class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cnt = k
        res = []
        for i in range(1, int(n ** .5) + 1):
            if n % i == 0:
                res.append(i)
                cnt -= 1
            if cnt == 0: return i
        # 倒序遍历因子
        # 特殊情况，完全平方数
        cnt += res[-1]**2 == n
        if cnt <= len(res): return n // res[-cnt]
        return -1 