class Solution(object):
    # 借助 散列表 + list 记录
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        records = dict()
        for index, i in enumerate(nums, 1):
            records[i] = records.get(i, -k)
            if (index - records[i]) <= k:
                return True
            records[i]=index
        
        return False

    # # 固定窗口的 set
    # def containsNearbyDuplicate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: bool
    #     """
    #     records = set()
    #     for i in range(len(nums)):
    #         if nums[i] in records:
    #             return True
    #         elif k and len(records) == k:
    #             # 如果 hash集合大小超过了 k 个， 删除最古老的那个元素
    #             print(i, k)
    #             records.remove(nums[i-k])
    #         records.add(nums[i])

    #     return False
    

A = Solution()
print(A.containsNearbyDuplicate([1,0,1,1], 0))