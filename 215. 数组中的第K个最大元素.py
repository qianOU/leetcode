class Solution:
    # 快排 找寻 第 k 大元素
    def findKthLargest(self, nums, k: int) -> int:
        n = len(nums)
        import random

        def find_k(left, right, k):
            # print(left, right,k, nums[left:right+1])
            idx = random.randint(left, right)
            nums[idx], nums[right] = nums[right], nums[idx]
            pre = left - 1 # 记录 大于 等于 阈值的 最右侧索引，初始话为 left - 1
            for i in range(left, right):
                # 因为找的 第 k 大的，所以将 大于 阈值的搬到左侧部分
                if nums[i] > nums[right]:
                    pre += 1
                    nums[i], nums[pre] = nums[pre], nums[i]
            pre += 1
            nums[pre], nums[right] = nums[right], nums[pre]
            # 注意！！！
            # 大于 nums 的区间为 [left,  pre], 长度为 pre - left + 1
            if pre+1-left == k:
                return nums[pre]
            elif pre+1-left < k:
                return find_k(pre+1, right, k-(pre-left+1))
            else:
                return find_k(left, pre-1, k)

        return find_k(0, n-1, k)

print(Solution().findKthLargest([7,6,5,4,3,2,1],
5))