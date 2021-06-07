class Solution:
    # 愚蠢的想法，单指针，从后往前遍历 遇见 0 就将后面所有的 非 0 数字移动
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 倒序
        n = len(nums)
        p0 = pn = n-1
        alpha = 0
        while p0 >= 0:
            # 连续 0
            while p0 >= 0 and not nums[p0]:
                p0 -= 1

            tmp = p0
            p0 += 1
            end = pn + alpha
            for i in range(alpha):
                nums[p0] = nums[pn]
                p0, pn = p0+1, pn+1
            
            # 补 0 
            for i in range(p0, end):
                nums[i] = 0

            pn = tmp
            alpha += 1 # 非 0 的字符数
            p0 = tmp - 1

    # 思路二： 边走边统计 0 的个数，在 0 后的索引为 i 的值 覆盖到 i - count 处，最后count个 用 0 覆盖
    def moveZeroes(self, nums: List[int]) -> None:
        pass

    # 双指针
    #  [0, l] 表示已经处理好的序列
    # [l, r] 是 已知为0的序列
    # [r, n] 是待处理的序列
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = -1 # 指向的是已经处理好的序列尾部
        for r in range(n):
            if nums[r]:# 未处理的序列的第一个非 0 数字，要和 已处理好的序列尾部后一个元素交换
                nums[l+1], nums[r] = nums[r], nums[l+1]
                l = l+1