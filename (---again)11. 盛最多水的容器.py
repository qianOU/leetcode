# 注意与接雨水题目的差异
class Solution:
    # 双指针
    def maxArea(self, height) -> int:
        n = len(height)
        l, r = 0, n-1
        ans = 0
        while l <= r:
            ans = max(ans, (r-l)*min(height[l], height[r]))
            if height[l] < height[r]: l += 1
            else: r -= 1
        
        return ans
        
        # return countain


print(Solution().maxArea([8,7,2,1,2,3,6,1,8,6,2,5,4,8,3,7,0,1,2,3,4,0]))