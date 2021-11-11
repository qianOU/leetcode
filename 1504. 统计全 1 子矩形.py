class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # z: 1 代表列和， 0 代表行和
        dp = [[[0, 0] for _ in range(1+n)] for j in range(1+m)]
        for i in range(1, 1+m):
            for j in range(1, 1+n):
                if mat[i-1][j-1]:
                    dp[i][j][0] = dp[i][j-1][0] + 1
                    dp[i][j][1] = dp[i-1][j][1] + 1
        
        # 遍历右下角
        ans = 0
        for i in range(m, 0, -1):
            for j in range(n, 0, -1):
                tmp = n
                for c_len in range(dp[i][j][1]): # 从下往上扫描
                    tmp = min(tmp, dp[i-c_len][j][0]) # 一行与右边连续的 1的个数
                    ans += tmp
                    if not tmp: break
        return ans