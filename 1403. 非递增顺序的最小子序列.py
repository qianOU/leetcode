class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums) / 2
        nums = sorted(nums, reverse=True)
        sub = 0
        for i in range(len(nums)):
            if sub > total:
                return nums[:i]
            sub += nums[i]
        