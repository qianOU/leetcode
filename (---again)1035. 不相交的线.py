class Solution:
    # 错误的解法 !!!! 实际上是 求两个序列的最长公共子序列问题
    def maxUncrossedLines(self, nums1, nums2) -> int:
        from collections import defaultdict
        bound = defaultdict(list)
        for i, v in enumerate(nums2):
            bound[v].append(i)

        pairs = []
        for i, v in enumerate(nums1):
            for item in bound[v]:
                pairs.append((i, item))

        
        # 求最大不相交区间数
        pairs.sort(key = lambda x: (x[-1], x[0]))
        print(pairs)
        x = prev = -1
        count = 0
        for i, j in pairs:
            if j>prev and i>x:
                prev = j
                x = i
                count += 1
        
        return count
    
    # 动态规划解法 最长公共子序列问题
    # 每一个字符有两个选择， 1 是 在 lcs 中， 另外一个 是 不在 lcs 中
    # 只有 两个 指针指向的 字符都在 lcs 中时， lcs 长度才会 + 1
    # 否则 就是 至少有一个字符不在 lcs 中，lcs 长度最大的情况
    def maxUncrossedLines(self, nums1, nums2) -> int:
        m, n = len(nums1), len(nums2)
        # dp[i][j] 表示 nums1[0..i] 和 nums2[0...j] 的最长公共子序列的长度
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]: # 如果字符相等，则一定在公共子序列中
                    dp[i][j] = dp[i-1][j-1] + 1
                else: # 否则 nums1[i-1] 和 nums2[j-1] 两个字符中，至少有一个不在公共子序列中
                    dp[i][j] = max(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    )

        return dp[m][n]