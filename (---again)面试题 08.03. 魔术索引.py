class Solution:
    # 单次遍历 没有使用有序的先验条件
    def findMagicIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i]==i: return i
        
        return -1

    # 分治！！！ # 找寻第一个 0
    # 中序遍历 
    def findMagicIndex(self, nums: List[int]) -> int:
        # 因为要找到最靠前的 0 所以 需要 先对比 左部分 是否搜寻到 0
        # 其次是 中间值 是否等于 0 
        # 最后是 右半部分是否等于 0 
        def get_answer(num, left, right): # 左闭右闭区间
            # 递归出口
            if left > right: return -1
            mid = left + (right - left >> 1)

            lv = get_answer(num, left, mid-1) 
            if lv != -1:
                return lv
            elif num[mid] == mid:
                return mid
            else:
                return get_answer(num, mid+1, right)
            
        
        return get_answer(nums, 0, len(nums) - 1)



