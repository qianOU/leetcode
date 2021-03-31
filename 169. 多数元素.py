class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        a = dict()
        for i in nums:
            a[i] = a.get(i, 0) + 1
            if a[i] > n/2:
                return i