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
        
        return l # 因为 上述循环的递归出口是 l>=r 且 nums[l] == val


