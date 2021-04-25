class Solution:
    # 单调队列
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)

        for i in range(len(T)-1, -1, -1):
            # 确保栈是严格递减的
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            
            if stack: # 单调栈算法里面,需要先更新答案数组
                ans[i] = stack[-1] - i
            
            stack.append(i) # 其后,再将 i 入队列
        
        return ans