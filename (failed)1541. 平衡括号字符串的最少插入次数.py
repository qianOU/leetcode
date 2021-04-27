class Solution:
    def minInsertions(self, s: str) -> int:
        stack1 = [] # (
        stack2 = [] # )
        for i in range(len(s)):
            if s[i] == '(':
                stack1.append(i)
            else:
                if stack1:
                    left = stack1.pop()
                    if stack2 and stack2[-1] > left:
                        stack2.pop()
                        continue
                    else:
                        stack1.append(left)
                
                stack2.append(i)
        
        print(stack1)
        print(stack2)
        
        if stack1 and stack2 and stack[-1] < stack2[-1]:
                return 1
        else:
                return 2 * len(stack1)  + stack2[-1]//2 + stack2[-1]%2*2
