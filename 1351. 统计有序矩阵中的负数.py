class Solution:
    def countNegatives(self, grid) -> int:
        # 二分查找 闭区间
        # 找寻的是 大于等于0 的第一个索引
        def binsearch(l, r, target, nums):
            if l > r: return
            lo, ro = l, r
            while lo <= ro:
                mid = (lo + ro) // 2
                if nums[mid] >= target: lo = mid + 1
                else: ro = mid - 1
            
            return ro 
        
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            idx = binsearch(0, n-1, 0, grid[i]) + 1
            ans += n - idx
            print(i, idx, ans)

        return ans


print(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))