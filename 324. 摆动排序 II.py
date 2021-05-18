class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return 
        # 找寻第target位大的值, target ：为数组第 target 个元素 【从 1 开始】
        # 对于本题 而言我们选择 中位数 + 1 的位置
        def quick_select(l, r, target):
            import random
            if l > r:
                return 
            mid = random.randint(l, r)
            K = nums[mid]
            nums[mid], nums[r] = nums[r], nums[mid]

            p = l - 1 # 确保 [l,...p] 都是 小于等于 K的
            for i in range(l, r):
                if nums[i] <= K:
                    p += 1
                    nums[p], nums[i] = nums[i], nums[p]
            p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p - l + 1 == target:
                return nums[p]
            elif p - l + 1 > target:
                return quick_select(l, p-1, target)
            else:
                return quick_select(p+1, r, target-(p-l+1))
        
        # 三指针实现局部有序
        def merge(nums, value):
            l, i, r = 0, 0, len(nums)-1
            while i<=r:
                if nums[i] < value:
                    nums[l], nums[i] = nums[i], nums[l]
                    i += 1
                    l += 1
                elif  nums[i] > value:
                    nums[i], nums[r] = nums[r], nums[i]
                    r -= 1
                else:
                    i += 1

        # nums.sort() # 时间复杂度为 0(NlogN)
        n = len(nums)
        mid = n // 2 if n%2 ==0 else (n+1) // 2
        quick_select(0, n-1, mid)
        
        value = nums[mid]
        res = nums.copy()
        merge(res, value)


        for i in range(1, n, 2):
            nums[i] = res[n  - (i+1)//2] # 偶数位 逆序插入
        for i in range(0, n, 2):
            nums[i] = res[mid-1 - i//2] # 奇数位逆序i插入   





