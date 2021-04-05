class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while  left <= right:
            print(left, right)
            mid = left + int((right-left)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        print(left, right)
        return -1

print(Solution().search( [-1,0,3,5,9,12], 9))