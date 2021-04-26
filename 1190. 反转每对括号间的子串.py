class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            
            if  i == ')':
                res = []
                while stack and stack[-1] != '(':
                    item = stack.pop()
                    res.append(item)
                
                if stack:
                    stack.pop() # 去除 '('
                
                
                stack.extend(res) # 重新入栈
            
            else:
                stack.append(i)
        return ''.join(stack)