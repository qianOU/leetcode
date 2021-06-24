class Solution:
    # 大神思路： 巧妙的翻转数组
    # 这道题 使用指针是难以处理的
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        res = k % n
        def reverse(l, r): # l, r 都是闭区间
            while l < r:
                nums[l], nums[r] = nums[r]. nums[l]
                l, r = l+1, r-1
            
        # step1 : 整体翻转
        reverse(0, n-1)
        # step2: 翻转前 res 个元素
        reverse(0, res-1)
        # step3: 翻转 res 之后的元素
        reverse(res, n-1)


        
