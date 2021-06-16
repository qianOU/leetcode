class Solution:
    # 二分， 因为峰值一定是在 凸函数的顶点处
    def findPeakElement(self, nums) -> int:
        n = len(nums)
        l, r = 0, n-1
    
        while l < r:
            mid = l + (r-l)//2
            # 局部减序，峰值点在[l， mid]中，注意是包含 mid 的因为 mid 处也可能是制高点
            if nums[mid] > nums[mid+1]: 
              r = mid
            # 局部什序，峰值点在[mid+1， r]中，注意是不包含 mid 的因为 mid 处不可能是制高点
            else:
                l = mid + 1
        
        return r



print(Solution().findPeakElement([1,2,3,1]))