class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1].islower() and i==stack[-1].upper():
                stack.pop()
            elif stack and stack[-1].isupper() and i==stack[-1].lower():
                stack.pop()
            else:
                stack.append(i)
        
        return ''.join(stack)