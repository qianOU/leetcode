class Solution:
    # 思路 1：
    # 滑窗 + 窗口有序集合
    # 思路：枚举每一个位置作为右端点的时候，找到其对应的最靠左的左端点，满足区间中最大值与最小值的差不超过 limit
    def longestSubarray(self, nums, limit: int) -> int:
        from sortedcontainers import SortedList
        window = SortedList()
        
        n = len(nums)
        l = 0
        ans = 0
        # r 作为 窗口的右边界
        for r in range(n):
            window.add(nums[r])
            # 收缩窗口左边界，直到 l 使得 window[-1] - window[0] 第一个成立 
            while window[-1] - window[0] > limit:
                window.remove(nums[l])
                l += 1
            ans = max(ans, r-l+1)
            
        return ans
    
    # 思路2: 滑窗 + 单调队列
    # 需要两个单调队列 分别用以 维护滑窗的 最大，小值
    def longestSubarray(self, nums, limit: int) -> int:
        from collections import deque
        qmax, qmin = deque(), deque()
        ans = l = 0

        for idx,r in enumerate(nums):
            # 维护窗口最大值
            while qmax and qmax[-1] < r: qmax.pop()
            # 维护窗口最小值
            while qmin and qmin[-1] > r: qmin.pop()

            qmax.append(r)
            qmin.append(r)

            # 查看窗口是否合法， 不合法的窗口收缩左边界
            # qmax[0] 是 [l... r] 作为窗口的时候的最大值
            while qmax[0] - qmin[0] > limit:
                # 如果要收缩的元素是极值，则极值也要更新
                if nums[l] == qmin[0]: qmin.popleft() 
                if nums[l] == qmax[0]: qmax.popleft()
                l += 1
            
            ans = max(ans,idx-l+1)

        return ans