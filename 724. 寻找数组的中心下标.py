class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 累计和
        total = sum(nums) # 总和
        sum_ = [0]
        for i in nums:
            sum_.append(sum_[-1]+i)
    

        for i in range(len(nums)):
            if sum_[i] == total - sum_[i+1]:
                return i
        
        return -1

print(Solution().pivotIndex( [ 1, -1,2 ])
)