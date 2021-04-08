class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        将所有元素绝对值作为数组下标，置对应数组值为负值。那么，仍为正数的位置即为（未出现过）
            消失的数字。
        '''
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0: # 如果已经置为 负数 则无需再乘以负数
                nums[abs(nums[i])-1] *= -1
        ans = []
        for i in range(1, len(nums)+1):
            if nums[i-1] > 0:
                ans.append(i)
        return ans