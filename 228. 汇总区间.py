class Solution(object):
    # 使用快慢指针。略微显得复杂
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [str(nums[0])]
               

        nums.append(float('inf'))
        res = []
        n = len(nums)
        slow = 0
        fast  = 1
        while fast < n:
            sep = nums[fast] - nums[fast-1]
            if sep > 1 and fast - slow > 1:
                res.append("%d->%d" %(nums[slow], nums[fast-1]))
                slow = fast
            elif sep > 1 and fast - slow == 1:
                res.append(str(nums[slow]))
                slow = fast
            fast += 1
        return res  

    def summaryRanges(self, nums): 
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [str(nums[0])]
        
        n = len(nums)
        res = []
        left = right = 0 # left, right 是控制区间左右两侧边界的
        while right < n:
            # 如果 right 和 left 指向的值 指相差 1的话，更新右边界
            # 循环结束 意味 着 一个区间的搜索完毕
            while right < n and nums[right] - nums[left] == right - left:
                right += 1
            
            if right - left == 1:
                res.append(str(nums[left]))
            
            else:
                res.append("%d->%d" %(nums[left], nums[right-1]))
            
            left = right
            
