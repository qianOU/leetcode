class Solution:
    # 排列组合的思维
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        more = [-1]
        less = []
        n = len(nums)
        for i in range(n):
            if nums[i] > right:
                more.append(i)
            elif nums[i] < left:
                less.append(i)

        more.append(n)
        ans = 0
        
        for i in range(1, len(more)):
            item = more[i] - 1 - more[i-1]
            ans += (item + 1) * (item) // 2

        
        r = 1
        l = res = 0
        m = len(less)
        while r < m:
            while r < m and less[r] == less[r-1] + 1:
                r += 1
            res += max((r  - l)*(r  - l + 1) // 2, r-l)
            l = r 
            r = r + 1

        if r == m:
            res += max((r  - l)*(r  - l + 1) // 2, r-l)

        return ans - res


    # 解法2：滑动窗口
    # 指针每次移动的时候只需要记录此刻的状态
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        n = len(nums)
        last_left = l = -1 # left 是左边界， last_left 窗口中最靠右的满足区间范围的索引位置
        ans = 0
        for r in range(n):
            if nums[r] <= right:
                if left <= nums[r]:
                    last_left = r # 更新 last_left
                    ans += r - l # 由于 r 本身也是符合区间范围的，所以是区间长度
                elif nums[r] < left:
                    ans +=last_left-l # r 必须和其最近的 符合区间范围的数结合在一块

            else:
                last_left = l = r
        

        return ans

    # 动态规划
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        n = len(nums)
        dp = [0]*(n+1) # dp[i] 表示以 nums[i] 为结尾的子数组数目
        rpos = -1
        for i in range(n):
            if nums[i] > right:
                dp[i] = 0
                rpos = i
            elif nums[i] < left:
                dp[i] = dp[i-1]
            else:
                dp[i]  = i - rpos

        return sum(dp)
    
    # 解法 4
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        def dfs(x): # count(x) 表示的是所有元素小于等于 x 的子数组数量
            ans = cur = 0
            for i in nums:
                # 以 i 为结尾的 符号要求的子数组数量为 cur
                cur = cur + 1 if i <= x else 0
                ans += cur
            return ans
        
        return dfs(right) - dfs(left - 1)



print(Solution().numSubarrayBoundedMax(
[427,277,795,647,735,752,185,896,459,261,632,868,337,595,529,168,469,590,606,578,19,403,575,892,691,725,127,761,119,366,616,403,983,433,155,173,899,247,654,154,366,749,474,312,95,619,796,701,451,328,520,564,55,529,769,74,768,693,639,442,400,617,851,245,419,862,821,103,663,799,349,785,920,662,318,418,668,959,671,684,209,879,194,70,122,662,667,622,558,288,505,63,304,977,809,84,853,611,865,96],
377,
772))

print(Solution().numSubarrayBoundedMax(
[2,9,2,5,6]
,2
,8
))