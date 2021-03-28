class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = right = 0
        while  right < len(nums)-1:
            right += 1
            if nums[right] != nums[right-1]:
                left += 1
                nums[left] = nums[right]
        
        return left + 1

A =Solution()
print(A.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))