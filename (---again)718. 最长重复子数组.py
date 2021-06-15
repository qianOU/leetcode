class Solution:
    #  正向 动态规划
    def findLength(self, nums1, nums2) -> int:
        m, n = len(nums1), len(nums2)
        # dp[i][j] 表示以 nums1[i] 为结尾 以及 以 nums2[j] 为结尾的 最长公共子数组长度
        dp = [[0]*(n+1) for i in range(m+1)]
        
        max_len = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 0

        return max_len


    #  逆序 动态规划 + 基于公共自字前缀概念
    def findLength(self, nums1, nums2) -> int:
        m, n = len(nums1), len(nums2)
        # dp[i][j] 表示以 nums1[i:] 以及 以 nums2[j:] 的最长公共子前缀长度
        dp = [[0]*(n+1) for i in range(m+1)]
        
        max_len = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 0

        return max_len
    
    #  滑动窗口解法 时间复杂度为 O((n+m)*min(n, m))
    # 分两步走
    # step1: 固定 B， 将 B中个元素 与 A 某个元素匹配对齐，
    # step2: 固定 A， 将 A中个元素 与 B 某个元素匹配对齐，
    def findLength(self, nums1, nums2) -> int:
        
        def maxLen(p1, p2, length):
            # length 是 p1 到 末尾的长度，以及p2 到某位长度的最小值
            ans = k = 0
            for i in range(length):
                if nums1[p1 + i] == nums2[p2 + i]:
                    k += 1
                    ans = max(ans, k)
                else:
                    k = 0

            return ans
        
        m, n = len(nums1), len(nums2)
        ans = 0
        # 固定 nums1
        for i in range(m):
            if nums1[i] == nums2[0]:
                length = min(m-i, n)
                if length <= ans:
                    break
                ans = max(ans, maxLen(i, 0, length))
        
        # 固定· nums2
        for i in range(n):
            if nums2[i] == nums1[0]:
                length = min(n-i, m)
                if length <= ans:
                    break
                ans = max(ans, maxLen(0, i, length))
        
        return ans