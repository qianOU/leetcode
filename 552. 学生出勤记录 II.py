class Solution:
    #思路1： 动态规划
    def checkRecord(self, n: int) -> int:
        import copy
        base = 10**9 + 7
        # 0 L 是第一次出现， 1： L是连续第二次出现： 2： 出现P
        dp =[[0, 0, 0, 0] for i in range(2)]
        # base case
        dp[0] = [1, 0, 1] # 序列没出现 A
        dp[1] = [0, 0, 0, 1] # 出现 A
        
        for i in range(1, n):
            tmp = copy.deepcopy(dp)
            
            dp[0][0] = tmp[0][2] % base
            dp[0][1] = tmp[0][0] % base
            dp[0][2] = sum(tmp[0]) % base

            dp[1][3] = sum(tmp[0]) % base
            dp[1][0] = (tmp[1][3] + tmp[1][2]) % base
            dp[1][1] =   tmp[1][0] % base
            dp[1][2] = sum(tmp[1]) % base

        return sum(sum(dp, [])) % base
    
    # 思路2: 矩阵快速幂
    def checkRecord(self, n: int) -> int:
        # dp 的状态浓缩到一位数组中
        # 状态转移矩阵 step[i][j] 表示从 i -- j
        step = [[0, 1, 1, 0, 0, 0, 0, 1],
                [0, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 1, 0]
 ]
        base = 10**9 + 7

        def matrix_mul(a, b): # 矩阵乘法 a * b
            m, tmp, n = len(a), len(a[0]), len(b)
            res = [[0]*n for i in range(m)]
            for i in range(m):
                for j in range(n):
                    for k in range(tmp):
                        res[i][j] += a[i][k] * b[k][j] 
                        res[i][j] %= base  # 求余
            return res
        
        # 矩阵快速幂
        def quick_mat_power(mat, n):
            ans = [[1, 0, 1, 0, 0, 0, 0, 1]]
            while n:
                if n & 1: ans = matrix_mul(ans, mat)
                mat = matrix_mul(mat, mat) # 矩阵翻一番
                n >>= 1 # 右移一位
            return ans
        
        return sum(quick_mat_power(step, n-1)[0]) % base


print(Solution().checkRecord(2))