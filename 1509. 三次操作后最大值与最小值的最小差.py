class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <=4:
            return 0

        nums.sort()

        # # 使用一次贪心是错误的思维方式
        # def get(k, left, right):
        #     if k==0:
        #         return nums[right] - nums[left]
            
        #     if nums[right] - nums[left+1] > nums[right-1] - nums[left]:
        #         return get(k-1, left, right-1)
        #     else:
        #         return get(k-1, left+1, right)
        
        # return get(3, 0, n-1)

        return min(nums[-1]- nums[3], nums[-2] - nums[2], nums[-3]-nums[1], nums[-4]-nums[0])