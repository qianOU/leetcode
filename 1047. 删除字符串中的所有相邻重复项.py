class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        p = 0
        while p < len(S):
            if stack and stack[-1]==S[p]:
                stack.pop()
                p += 1
            else:
                stack.append(i)
        
        return ''.join(stack)