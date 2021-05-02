class Solution:
    def mostCompetitive(self, nums, k: int):
        # 非严格单调递增栈
        stack  = []
        n = len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]: # 选择记录非递减序列
                if n -  i + len(stack) > k: # 明确 i索引及之后的所有元素入栈是否可以 使得最终获得k个元素的条件
                    stack.pop() # 若是可行解，则出栈，得到更具竞争力的解
                else:
                    break #否则 进行下一次对比
                
            stack.append(i)

        return [nums[i] for i in stack[:k]]


