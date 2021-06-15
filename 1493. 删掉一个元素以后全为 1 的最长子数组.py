class Solution:
    def longestSubarray(self, nums) -> int:
        n = len(nums)
        prev_count = 0 # 某一个0左侧连续 1的个数
        prev = 0 # 第一个非0的位置
        ans = 0 
        flag = 0 # 是否有0存在
        for i in range(n):
            if not nums[i]:
                flag = 1
                ans = max(ans, prev_count + i - prev)
                prev_count = i - prev
                prev = i + 1
                

        if nums[-1]:
            ans = max(ans, prev_count + n-prev)
        if not flag:
            ans -= 1
        return ans


print(Solution().longestSubarray(
 [0,1,1,1,0,1,1,0,1]))