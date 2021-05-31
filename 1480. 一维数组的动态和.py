class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        presum = [0]
        for i in nums:
            presum.append(presum[-1] + i)
        return presum[1:]