class Solution:
    # 方法一： 记录 每一个索引位置 左边 和 右边的最大值 作为桶边
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
    
    # 方法2 非严格单调递减栈
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]: # 必须是小于号，不能是小于等于号， 非严格的单调递减栈
                cur = stack.pop()
                if not stack: # 如果没有左边元素比 cur 对应的高度大时（即）cur为最大高度
                    break
                left = stack[-1]
                ans += (i - left - 1) * min(height[left]- height[cur], height[i]- height[cur])

            stack.append(i)
        return ans