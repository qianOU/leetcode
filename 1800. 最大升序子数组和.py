class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        ans = 0
        window = [nums[0]]
        while right < len(nums):
            window = []
            while right < len(nums) and nums[right] >= nums[left]:
                if nums[right] > nums[left] or right == left:
                    window.append(nums[right])
                    left = right
                    right += 1
                else:
                    break

                

            if sum(window) > ans:
                ans = sum(window)

            left = right
        return ans

    def maxAscendingSum(self, nums):
        ret = 0
        tmp = 0
        for i,j in enumerate(nums):
            if nums[i] > nums[i-1 if i>=1 else 0]:
                tmp += nums[i]
            else:
                ret = max(ret, tmp)
                tmp = nums[i]
        
        return max(tmp, ret)


print(Solution().maxAscendingSum([5,5,6,1,2,3,4,5,6,6,9,1,2]))