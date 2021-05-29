class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = [] # 与栈顶元素相同时入栈，不同时出栈
        count = 0
        for i in s:
            if not stack or stack[-1] == i:
                stack.append(i)
            if stack and stack[-1] != i:
                stack.pop()
            if not stack:
                count += 1
        return count