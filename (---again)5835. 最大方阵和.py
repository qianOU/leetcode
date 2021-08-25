class Solution:
    # 贪心
    # 负数符号是可以转移到矩阵任意位置
    # 如果有偶数位负数，则通过转移相乘，负数都会变成正数
    # 如果有奇数位负数，则将多余的一个负数转移到绝对值最小的数上，确保和最大
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res, count = float('inf'), 0
        ans = 0
        for item in matrix:
            for p in item:
                res = min(res, abs(p))
                if p < 0: count += 1
                ans += abs(p)
        
        if count & 1: return ans - 2*res
        return ans