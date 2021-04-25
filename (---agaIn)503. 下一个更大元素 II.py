class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 单调栈
        stack = []
        n = len(nums)
        res = [-1] * n
        for i in range(2*n-1, -1, -1):
            # 确保栈里是单调递减的
            while stack and nums[stack[-1]] <= nums[i%n]:
                stack.pop() 
     
            res[i%n] = nums[stack[-1]] if stack else -1 # 使用 i%n 之后的元素.来更新i%n后的最大元素
            stack.append(i%n) # 最后更新 stack 栈
               
        print(stack)
        return res