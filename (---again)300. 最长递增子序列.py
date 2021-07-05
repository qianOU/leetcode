class Solution:
    # 纯动态规划解法 0（n**2）
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] 表示的是以 nums[i] 为结尾的最长递增子序列的长度
        dp = [1]*n
        ans = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        
        return ans

    # 贪心 + 二分方法
    # 贪心的规则为了获得最长 LIS，因此每次都填入比上个元素大一点点的元素
    # 二分 主要涉及到 tails 数组具有单调性
    # 详细见 大佬题解
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # 这给 tails 定义的十分巧妙，确定了有序性！！！！
        tails = [] # tails[i] 表示的是 长度为 i+1 的 LIS 尾部元素
        for i in range(n):
            # 二分查找，tails 中尾部元素第一个 大于 nums[i] 的位置，并且改为 nums[i](为了LIS序列最长化)
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] >= nums[i]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 找到想要的位置
            if  l < len(tails): tails[l] = nums[i]
            else: tails.append(nums[i])
        
        return len(tails)

