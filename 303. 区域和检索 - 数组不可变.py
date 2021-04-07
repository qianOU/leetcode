class NumArray:

    def __init__(self, nums: List[int]):
        self.prenums = [0]*(1+len(nums))
        for i in range(1, len(nums)+1):
            self.prenums[i] = self.prenums[i-1] + nums[i-1] # self.prenums[i] 表示 nums[0...i-1] 的闭区间的和


    def sumRange(self, left: int, right: int) -> int:
        return self.prenums[right+1] - self.prenums[left]
