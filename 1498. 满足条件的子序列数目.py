class Solution:
    def numSubseq(self, nums, target: int) -> int:
        nums.sort()
        mod = 10**9 + 7

        # 二分查找， 找到 小于等于 t-a 的右边界
        def bin_search(l, r, a): # 左闭右闭区间
            if l > r:
                return   
            t = target - a
            lo, ro = l, r
            while lo <= ro:
                mid = (lo + ro) // 2
                if nums[mid] > t:
                    ro = mid - 1
                elif nums[mid] <= t:
                    lo = mid + 1
            return ro

        l, r = 0, len(nums) - 1
        ans = 0
        while l <= r:
            idx = bin_search(l, r, nums[l])
            ans += 2**(idx-l) if idx >=l else 0
            # print(ans, idx, l, r)
            l += 1
            r = idx
            
        
        return ans % mod