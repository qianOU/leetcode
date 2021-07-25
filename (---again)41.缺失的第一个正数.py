class Solution:
    # 数组hash表
    def firstMissingPositive(self, nums: List[int]) -> int:
        n  = len(nums)
        for i in nums:
            if i is None or i > n or i <= 0: continue
            cur = i
            while cur and 0 < cur <= n:
                nums[cur-1], cur = None, nums[cur-1]

            nums[i-1] = None

        for i in range(n):
            if nums[i] is not None: return i + 1
        
        return n+1
    
    # 交换位置
    def firstMissingPositive(self, nums: List[int]) -> int:
        n  = len(nums)
        for i in range(n):
            # 将 如果 nums[x] 在[1...n] 中， 将 nums[nums[x]-1] 与 nums[x] 形成对应
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(n):
            if nums[i] != i + 1: return i + 1
        return n + 1
