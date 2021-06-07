class Solution:
    def subsets(self, nums):
        n = len(nums)
        
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i): # 表示以nums[i] 为结尾的子集序列
            ans = [[nums[i]]]
            if i == 0: 
                return [[nums[i]]]
            for j in range(i-1,-1,-1):
                for tmp in dfs(j):
                    tmp = tmp.copy()
                    tmp.append(nums[i])
                    ans.append(tmp)
            return ans

           
        ans = [[]]
        for i in range(n):
            ans.extend(dfs(i))
    
        return ans


    
print(Solution().subsets([1,2,3]))