class Solution:
    def minMoves(self, nums) -> int:
        return sum(nums) - min(nums) * len(nums)
print(Solution().minMoves([5,6,8,8,5]))