class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        ans = []
        for i in nums:
            if i%2:
                odd.append(i)
            else:
                even.append(i)
        
        for i in range(len(even)):
            ans.append(even[i])
            ans.append(odd[i])
        
        return ans