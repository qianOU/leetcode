class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = [-1] * n
        right_max = 0
        # 记录 i 右边 的最大值
        for i in range(n-1, -1, -1):
            res[i] = max(right_max, height[i])
            right_max = res[i]
        ans = 0
        # 记录 i 左边的最大值
        left_max = 0
        for i in range(n):
            item = min(left_max, res[i])
            ans += max(item - height[i], 0) # 更新答案
            left_max = max(left_max, height[i])
        
        return ans