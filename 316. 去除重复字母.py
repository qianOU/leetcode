class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        import collections 
        counter = collections.Counter(s)
        stack = [] # 单调递增栈

        for i in s:
            if i not in stack: # i 不在栈中时（去重）
                while stack and stack[-1] >= i and counter[stack[-1]] > 0: # 计数大于 0 是确保之后可以再次入栈
                    stack.pop()

                stack.append(i)
            counter[i] -= 1

        return ''.join(stack) 