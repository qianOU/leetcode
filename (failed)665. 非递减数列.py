class Solution:
    def checkPossibility(self, nums) -> bool:
        n = len(nums)
        if n == 1: return True

        
        k = 1 if nums[0] <= nums[1] else 0 
        for i in range(2, n):
            if nums[i-1] > nums[i]:
               
                if not k: return False
                tmp = nums[i+1] if i < n-1 else 100000
                if nums[i-1] > tmp and not k: return False
                elif nums[i-1] <= tmp:
                    nums[i] = nums[i-1]
                print(i, nums, k)
                
                k -= 1
            
           
        
        return True


print(Solution().checkPossibility([3,4,2,3]))