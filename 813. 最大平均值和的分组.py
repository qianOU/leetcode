class Solution:
    def largestSumOfAverages(self, nums, k: int) -> float:
        n = len(nums)
        presum = [0] # 前缀和
        for i in nums:
            presum.append(presum[-1] + i)
        
        dp = [[float('-inf')]*(1+n) for i in range(k)] # dp[i][j]表示第i个分割位置是j的时候，已知最大平均值总和
        # base case
        dp[0][0] = 0
        for i in range(1, k):
            for j in range(i, n-(k-i)+1):
                dp[i][j] = max(dp[i-1][p] + (presum[j] - presum[p]) / (j-p) for p in range(j))
        
        return  max(dp[k-1][p] + (presum[n] - presum[p]) / (n-p) for p in range(n))


print(Solution().largestSumOfAverages(
[1,2,3,4,5,6,7]
,4
))