class Solution:
    # 时间优先 使用集合
    def findRepeatNumber(self, nums) -> int:
        path = set()
        for i in nums:
            if i in path: return i
            path.add(i)
    
    # 空间优先：原地排序 指针找到是否有连续出现字符
    def findRepeatNumber(self, nums) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: return nums[i]
    
    # O(n) 原地修改数组 
    # 注意到： 索引和数组值是 1 vs 多 关系，
    # 因此 如果 nums[i] != i 的时候，可以先交换 nums[nums[i]] 和 nums[i] 的值，使得索引和值对应
    # 如果有重复 就是 指存在两个不同的索引 nums[i] 和 i 都指向 同一处 i
    # PS 因为首次遇见的元素 i 都已经与 索引i i 对齐了
    def findRepeatNumber(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == i: continue
            if nums[nums[i]] != nums[i]: # 首元素和索引不对齐的情况
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]] # 注意交换的顺序
            else: return nums[i]

    # O(n) 原地修改数组 使用 + = 进行区分，因为有 0 所以需要先对数组值 +1 先

    