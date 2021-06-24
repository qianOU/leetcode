class Solution:

    #由相关题目联想到：  贪心 找寻 最右侧的左边界位置 + 快排
    # 效率 不高， 实际上有更加巧妙的双指针解法！！！（实在妙！）
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 快排
        def quick( left, right):
            if left >= right:
                return
            l, r = left + 1, right
            while l <= r:
                while l <= r and nums[l] < nums[left]:
                    l += 1
                while l <= r and nums[r] > nums[left]:
                    r -= 1
                if l >= r:
                    break
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
            # nums[r] 一定是小于等于 nums[left] 的， 而 nums[l] 则 可能 大于等于 nums[left]
            # 因此 left 和 r 交换位置 
            nums[r], nums[left] = nums[left], nums[r]
            quick(left, r-1)
            quick(r+1, right)

        # left 记录了 可以增大 排列 的，最右侧的左边界交换位置
        left = -1 
        for i in range(n-1, 0, -1):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    if j > left: # 如果左边界更靠右，离 i 更近
                        left = j
                        right = i
                        break

                if nums[j] == nums[i]:
                    break
        
        if left >= 0:
            nums[left], nums[right] = nums[right], nums[left]
            quick(left+1, n-1) # 因为允许交换多次，左边界left确定了最右侧可以使得排列变大最小变化的交换位置，为了整体能得到最小，所以需要右侧也从小到大变化，这样子就是符合题意的答案了
            return
        
        quick(0, n-1)

    # 思路：
    # step1： 找寻一个左边的【较小数】并且使其尽量靠近右侧
    # step2： 找寻右侧的一个【较大数】要求尽可能小
    # step3： 将较大数包括其本身位置，保持升序
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # step1 : 从后往前找 第一个 递减的位置 i
        left = None
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                left = i-1
                break

        if left is not None:
            # step2 ： [left+1, n-1] 区间内是单调递减的
            # 使用二分查找， 第一个 大于 nums[left] 的元素（大于 nums[left] 的右边界）
            l = left + 1
            r = n - 1
            while l <= r:
                mid = (l + r)//2
                if nums[mid] > nums[left]:
                    # 所有满足 nums[mid] > nums[left], 的都有 mid = l - 1
                    # 由于我们要找 第一个 大于 nums[left] 的索引，其也满足 l - 1 的规律
                    l = mid + 1
                else:
                    r = mid - 1
            # 找到的第一个 大于 nums[left] 的索引记为 right
            right = l - 1 # l-1 =
            print(left, right)
            # 交换
            nums[left], nums[right] = nums[right], nums[left]
            
        else:
            left = -1
        
        # step3: 保证 right 及其右侧是单调递增的
        # 由于之前是单调递减的急，因此只需要双指针交换位置即可，不需要真的排序
        l, r = left+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1




print(Solution().nextPermutation([1,3,2]))