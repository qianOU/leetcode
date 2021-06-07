class Solution:
    def check(self, nums) -> bool:
        bucket = [0]*101
        for i in nums:
            bucket[i] += 1
        
        j, n = 0, len(nums)
        flag = 0
        while j < n:
            for v in range(nums[j], 101):
                # print(v, bucket[v])
                if  bucket[v] is None: 
                    return False
                if j<n and nums[j]!=v: return False
                while j<n and nums[j] == v and bucket[v]:
                    j+=1
                    bucket[v] -= 1
                
                bucket[v] = None if not bucket[v] else bucket[v]
                if j == n or flag > 1: break
                if nums[j]<v: 
                    print(j,v,bucket[v], flag)
                    flag += 1
                    break
            print(j, flag)
        return flag < 2


print(Solution().check([1,3,2]))