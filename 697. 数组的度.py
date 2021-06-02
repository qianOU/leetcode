class Solution:
    def findShortestSubArray(self, nums) -> int:
        from collections import defaultdict
        dic = defaultdict(list)
        n = len(nums)
        for i in range(n):
            dic[nums[i]].append(i)
        
        print(dic)
        ans, most =n, 0
        for a in dic.values():
            if len(a) > most:
                most = len(a)
                ans = a[-1]-a[0]+1
            elif len(a) == most:
                ans = min(a[-1]-a[0]+1, ans) 
            print(most, a)
        return ans


print(Solution().findShortestSubArray([1,2,2,3,1,4,2]))