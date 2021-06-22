class Solution:
    def partitionDisjoint(self, nums) -> int:
        r_parts = [nums[-1]] 
        l_parts = [nums[0]]
        n = len(nums)
        for i in range(n-2,-1,-1):
            r_parts.append(min(r_parts[-1], nums[i]))
        
        for i in range(1, n):
            l_parts.append(max(l_parts[-1], nums[i]))
        
        
        print(r_parts)
        print(r_parts[::-1])
        print(l_parts)

        for i in range(1, n):
            # l_parts 部分指的是 以 [0,...i-1] 的左部分的最大值，
            # r_parts[n-1-i] 指的是 以 [i,..n-1] 为区间的有部分的最小值
            if  l_parts[i-1] <= r_parts[n-1-i]:
                return i
        return n


print(Solution().partitionDisjoint([1,1]))