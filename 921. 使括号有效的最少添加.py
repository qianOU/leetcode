class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        # 换言之就是找寻有几个括号是不合法的
        stack = []
        for i in S:
            if i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        
        return len(stack)