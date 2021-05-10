class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # items = sorted((j, i) for i,j in enumerate(nums))
        # arr = [i[0] for i in items]
        # map_ = {o:n for n, (_, o) in enumerate(items)}


        res = [True] * len(l)
        for i in  range(len(l)):
            left, right = l[i], r[i]
            sub = None
            arr = sorted(nums[left:right+1])
            for j in range(right-left):
                if sub is None:
                    sub = arr[j+1] - arr[j] 
                elif sub != arr[j+1] - arr[j]:
                    res[i] = False
                    break
        
        return res