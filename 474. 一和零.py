class Solution:
    # 0-1 背包问题
    def findMaxForm(self, strs, m: int, n: int) -> int:
        res = []
        for i in strs:
            count_1 = sum(j == '1' for j in i)
            res.append((len(i) - count_1, count_1))
        
        dp = [[[0]*(1+n) for i in range(1+m)] for j in range(1 + len(strs))]
        # base case
        ans = 0

        for row in range(1, 1 + len(strs)):
            for i in range(1+m):
                for j in range(1+n):
                    cun0, cun1 = res[row-1]
                    dp[row][i][j] = dp[row-1][i][j] # 不选 row 时。
                    if i >= cun0 and j >= cun1: #如果可以选择row的时候，要选最优的
                        # 两个状态，选 row【dp[row-1][i-cun0][j-cun1] + 1】，不选 row 【dp[row-1][i][j]】
                        dp[row][i][j] = max(dp[row-1][i-cun0][j-cun1] + 1, dp[row-1][i][j])
                    
        return dp[len(strs)][m][n]

    # 优化：滚动数组优化空间
    def findMaxForm(self, strs, m: int, n: int) -> int:
        res = []
        for i in strs:
            count_1 = sum(j == '1' for j in i)
            res.append((len(i) - count_1, count_1))
        
        dp = [[0]*(1+n) for i in range(1+m)]
        
        for row in range(len(strs)):
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    cun0, cun1 = res[row]
                    if i >= cun0 and j >= cun1:
                        dp[i][j] = max(dp[i-cun0][j-cun1] + 1, dp[i][j])
        return dp[m][n]

from pprint import pprint

print(Solution().findMaxForm(
["0","0","1","1","1","0","1","0","0","1","1","0","1","0","1","0","1","0","0","1","0","1","0","0","1","1","1","0","1","1","0","0","1","1","1","0","1","0","0","0","1","0","1","0","0","1","0","0","1","1","1","1","1","0","0","1","0","1","0","1","1","0","0","0","1","1","1","1","1","1","0","1","1","1","0","0","1","1","0","0","1","1","0","1","0","0","1"]
,93,
91))
