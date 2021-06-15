class Solution:
    # 动态规划，状态定义十分重要
    def lenLongestFibSubseq(self, arr) -> int:
        v2index = {j:i for i,j in enumerate(arr)}
        n = len(arr)
        # dp[i][j] 表示的是以 arr[i],arr[j]作为最后两项的最长斐波那契数列的长度
        # base case 对于 任意 i<j 都有 dp[i][j] == 2
        dp = [[2]*n for i in range(n)]

        ans = 2
        for i in range(n-1):
            for j in range(i+1, n):
                k = v2index.get(arr[j] - arr[i])
                if k is not None and k < i: # 必须要求 k 是小于 i 的
                    dp[i][j] = dp[k][i] + 1
                    ans = max(dp[i][j], ans)
        
        return ans if ans > 2 else 0