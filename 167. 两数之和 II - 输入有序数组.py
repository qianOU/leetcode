class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers)<=1:
            return 
        left = 0
        right = len(numbers)-1

        while left <= right: # 左右皆为闭区间
            sum_l = numbers[left]
            sum_r = numbers[right]
            sum_ = sum_l + sum_r
            if sum_ > target:
                while left <= right and sum_r == numbers[right]:
                    right -= 1
            elif sum_ < target:
                while left<=right and sum_l == numbers[left]:
                    left += 1
            else:
                return [left+1, right+1]


A = Solution()
print(A.twoSum([2,7,11,15], 9))