class Solution:
    # 位运算
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for i in nums:
            x ^= i # 得到两个不同数字的异或值
        # 得到 x 的 最低位 为 1 的 位置c(因为是不同的数字，所以一定存在 1)
        c = 0
        while not ((x >> c) & 1):
            c += 1
        
        # 实际上我们不需要移动数组，找寻分割两个子数组的点
        #可以直接用 a，b 表示两个子数组的值，进行异或即可
        a = b = 0
        for i in nums:
            if (i >> c) & 1:
                b ^= i
            else:
                a ^= i
        # l, r = 0, len(nums) - 1
        # # l 指向的是 c 位置为 0 的元素， r 指向的 是 c 位置为 1 的 元素
        # # [0,...l-1] 指向的是 c 位置为 0 的元素, [l(r+1),..n-1]  指向的是 c 位置为 1 的元素
        # while l <= r: # 这里需要加入等于号
        #     if (nums[l] >> c) & 1:
        #         nums[r],nums[l] = nums[l], nums[r]
        #         r -= 1
        #     else:
        #         l += 1

        # from functools import reduce
        # a = reduce(lambda x, y: x^y, nums[:l], 0)
        # b = reduce(lambda x, y: x^y, nums[l:], 0)
        return [a, b]


