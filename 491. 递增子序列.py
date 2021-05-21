class Solution:
    def findSubsequences(self, nums) :
        if not nums:
            return [[]]

        n = len(nums)
        ans = []
        def dfs(i, path):
            if len(path) >= 2:
                ans.append(path.copy())
            visited = set()
            for j in range(i+1, n):
                if  nums[j] not in visited and path[-1] <= nums[j] :
                    visited.add(nums[j])
                    path.append(nums[j]) 
                    dfs(j, path) # nums[j] 是某位序列位置
                    path.pop()

                
        visited = set()
        for i in range(n):
            if nums[i] not in visited:
                visited.add(nums[i])
                dfs(i, [nums[i]])

        return ans