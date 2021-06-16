class Solution:
    # 滑动窗口 + 间隔差数组
    def maxTurbulenceSize(self, arr) -> int:
        cross = []
        n = len(arr)
        if n == 1: return 1

        for i in range(1, n):
            cross.append(arr[i] - arr[i-1])
        
        # 如果 cross 里面有非0存在，也就意味着答案最少为2，否则为1 
        ans = 2 if any(cross) else 1
        l = 0
        for i in range(1, n-1):
            if cross[i-1] * cross[i] < 0:
                ans = max(ans, i-l+2)
            else: #收缩左边界
                l = i
        
        return ans
    
    # 动态规划 Dp
    def maxTurbulenceSize(self, arr) -> int:
        n = len(arr)
        if n == 1: return 1

        dp = [0]*n # dp[i] 表示以 arr[i] 为结尾的最长湍流子数组长度
        #base-case
        dp[0] = 1
        dp[1] = dp[0] + 1 if arr[1] - arr[0] else 1

        for i in range(2, n):
            if (arr[i] - arr[i-1]) * (arr[i-1] - arr[i-2]) < 0:
                dp[i] = dp[i-1] + 1
            elif  arr[i] - arr[i-1]:
                dp[i] = 2
            else:
                dp[i] = 1
        
        return max(dp)


print(Solution().maxTurbulenceSize([9,9,9,12]))

