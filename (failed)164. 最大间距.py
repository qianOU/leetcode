class Solution:
    # 单调栈
    
    # 计数排序 超时
    def maximumGap(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return 0
        max_, min_ = max(nums), min(nums)
        ans = [0] * (max_-min_+1)
        length = 0

        for i in range(n):
            ans[nums[i]-min_] += 1
        

        prev = flag = 0
        for i in range(max_-min_+1):
            if flag and ans[i]:
                length = max(i-prev, length)
                flag = 0
            if not flag and ans[i]:
                prev = i
                flag = 1
                
        
        return length

print(Solution().maximumGap([3,6,9,1]))