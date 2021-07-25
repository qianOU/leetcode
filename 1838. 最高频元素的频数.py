class Solution:
    # 写复杂了 排序 + 前缀差距累计数组(实际上用前缀和数组进行了) + 二分查询
    def maxFrequency(self, nums, k: int) -> int:
        nums.sort()
        n = len(nums)
        vis = set()
        # 预处 前缀差分数组 
        # predelta[i] 表示的是 从 第 0 个元素 到 第 i个元素的总的差距
        predelta = [0]*n

        # 计数数组
        from collections import defaultdict
        count = defaultdict(int)
        for i in range(n):
            count[nums[i]] += 1
 
        for i in range(1, n): #
            predelta[i] = predelta[i-1] + (nums[i] - nums[i-1]) * i

        ans = 0
        for idx, v in enumerate(nums): # 枚举最后递加的结果数
            if v in vis: continue
            vis.add(v)
            total = predelta[idx]
            l, r = 0, idx 
            while l <= r: # 二分查找符合条件的左边界
                mid = (l + r) // 2
                if predelta[mid] + k + mid*(nums[idx]-nums[mid]) >= total:
                    r = mid - 1
                else: l = mid + 1
            
            ans = max(ans, count[v] + idx - l)
            
        return ans
    
    # 实际上本题具有滑动窗口特性,不需要进行二分查找  (写的冗余了)
    def maxFrequency(self, nums, k: int) -> int:
        nums.sort()
        n = len(nums)
        if n == 1: return 1
        l, r = 0, 1
        ans = 0
        window = nums[1] - nums[0]
        while r < n:
            
            while r < n  and window <= k:
                r += 1
                if r >= n: break
                window +=  (nums[r] - nums[r-1]) * (r - l)
            
            ans = max(ans, r - l)

            if r < n:   
                window -= nums[r] - nums[l]
                l += 1

        return ans
    
    # 滑动窗口 简洁写法
    def maxFrequency(self, nums, k: int) -> int:
        nums.sort()
        n = len(nums)
        window = 0
        l = 0
        ans = 1
        for r in range(1, n):
            window += (nums[r] - nums[r-1]) * (r - l)
            while window > k:
                window -= nums[r] - nums[l]
                l += 1

            ans = max(ans, r - l + 1)
        
        return ans

print(Solution().maxFrequency(

[1,4]
,5
))