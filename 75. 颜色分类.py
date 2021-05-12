class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 特殊的三指针的快排
        def quick(left, right): # 左闭右开的区间
            """
            [left, lo-1] 是 v == 0 的部分
            [lo, i-1] 是 v == 1 的部分
            [i, gt-1] 是 未定部分
            [gt, right) 是 v == 2 的·部分
            """
            if left >= right:
                return 
            
            lo = i = left
            gt = right - 1

            while i <= gt:
                if nums[i] < 1:
                    nums[i], nums[lo] = nums[lo], nums[i]
                    lo += 1
                    i += 1
                elif nums[i] == 1:
                    i += 1
                else:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
            
        
        quick(0, len(nums))
        
