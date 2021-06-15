class Solution:
    def findMin(self, nums) -> int:
        # 二分查找
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l)//2
            print(l, mid, r, nums[l], nums[mid], nums[r])
            if nums[l] > nums[r] >= nums[mid]:
                l, r = l-1, mid 
            elif nums[mid] >= nums[l] > nums[r]:
                l, r = mid+1 , r
            elif nums[r] > nums[mid] >= nums[l]:
                l, r = l, mid - 1
            elif nums[r] > nums[mid] >= nums[l]:
                l, r = l, mid - 1



        return nums[l]

print(Solution().findMin([5,1,2,3,4]))