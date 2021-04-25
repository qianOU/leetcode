class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = []
        for i in S:
            if i==')':
                item = stack.pop()
                if stack: # 出栈时,如果不是退出最外层括号,则存入数组
                    res.append(')')
                
            else:  
                if stack: # 进栈时,如果不是第一个 ( 则进栈
                    res.append(i) 
                stack.append(i)
                
        return ''.join(res)

print(Solution().removeOuterParentheses("((()))"))