class Solution:
    # 思路1： 滑动窗口(写的不够精简！！！，当右指针停止移动的时候，可以使用while 控制左指针直到不符的情况)
    def minSubArrayLen(self, target: int, nums) -> int:
        ans = float('inf')
        l = r = 0
        window = 0
        n = len(nums)
        # 退出循环的标志是： 右指针移动到右边界，并且 window 的值已经小于 target的时候，就不需要再移动指针了
        while r!=n or window >= target:
            # 当窗口的值 大于等于 target的时候，停止移动右指针
            while r < n and window < target:
                window += nums[r]
                r += 1
            # 符合条件的情况下，更新答案
            if window >= target:
                ans = min(ans, r - l)

            # 开始 收缩左边界
            window -= nums[l]
            l = l+1

        return ans if ans != float('inf') else 0

    # 思路2： 滑动窗口（优美的写法）
    def minSubArrayLen(self, target: int, nums) -> int:
        ans = float('inf')
        l = r = 0
        window = 0
        n = len(nums)

        while r < n:
            window += nums[r]

            # 通过 while 控制左指针一直移动到 window < target 为止
            while window >= target:
                ans = min(ans, r-l+1)
                l += 1

            r += 1 # 移动右指针

        return ans if ans != float('inf') else 0
    
    # 思路2：前缀和 + 二分
    def minSubArrayLen(self, target: int, nums) -> int:
        n = len(nums)
        presum = [0]
        for i in nums:
            presum.append(presum[-1] + i)
        
        l, r = 1, n
        ans = 0
        while l <= r:
            mid = (l + r)//2
            for i in range(1, n-mid+2):
                value = presum[i+mid-1]-presum[i-1]
                if value >= target:
                    r = mid - 1
                    ans = mid
                    break
            else:
                l = mid + 1
        
        return ans




print(Solution().minSubArrayLen(
7,
[2,3,1,2,4,3]
))
