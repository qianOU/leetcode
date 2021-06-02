class Solution:
    def removeElement(self, nums, val: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            while l <= r and nums[l]!=val:
                l+=1
            while l <= r and nums[r] == val:
                r -= 1
            
            if l >= r: break

            nums[l], nums[r] = nums[r], nums[l]
        
        return l


print(Solution().removeElement(
 [0,1,2,2,3,0,4,2], val = 2
))