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

    # # 固定窗口的 set 的大小为 k-1 ，则下一个数字如果出现在 set 中，就是 符合 i - j 的绝对值小于等于 k
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0: return False

        records = set()
        for i in range(len(nums)):
            if nums[i] in records:
                return True
            elif  len(records) == k:
                # 如果 hash集合大小 >= k 个， 删除最古老的那个元素
                records.remove(nums[i-k])

            records.add(nums[i])

        return False
    

A = Solution()
print(A.containsNearbyDuplicate([1,2,3,1,2,3], 2))