class Solution:
    # 贪心 只需要关注于 一个元素
    # 如果前一个元素 大于等于 后一个元素
    # 则将后一个元素更新为 前 一个元素 + 1（每步贪心走最小
    def minIncrementForUnique(self, nums) -> int:
        if not nums: return 0
        seen = set()
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(1, n):
            if nums[i] <= nums[i-1]: # 如果前一个元素 大于等于 后一个元素
                tmp = nums[i]
                nums[i] = nums[i-1] + 1 # 则将后一个元素更新为 前 一个元素 + 1（每步贪心走最小步）
                ans += nums[i] - tmp
                

        return ans