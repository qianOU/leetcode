class Solution:
    # 单调栈的变形
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        visited = set() # 记录是否在栈中
        
        import collections
        nums = collections.Counter(s)

        for i in s:
            if i not in visited: # 如果还没有遍历过
                # 单调递增栈，与字典序对应
                # 确保弹出的栈顶元素,之后有再次加入的可能，即 num[stack[-1]] > 0
                while stack and i < stack[-1] and nums[stack[-1]] > 0:
                    visited.discard(stack[-1])
                    stack.pop()

                stack.append(i)
                visited.add(i)
            nums[i] -= 1
        
        return ''.join(stack)



        

