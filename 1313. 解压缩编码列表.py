class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        from functools import reduce
        return reduce(lambda x,y :x+y, [[nums[i+1]]*nums[i] for i in range(0, len(nums), 2)])

