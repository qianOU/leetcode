class Solution:
    def minPairSum(self, nums: List[int]) -> int:
      nums.sort()
      n = len(nums)
      return max(nums[i]+nums[n-1-i] for i in range(n//2))  