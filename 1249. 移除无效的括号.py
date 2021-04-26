class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack1 = [] # 存放 '(' 索引
        stack2 = [] # 存放 ')' 索引
        res = []
        for i in range(len(s)):
            s1 = s[i]
            if s1 == '(':
                stack1.append(i)
            if s1 == ')':
                if stack1:
                    stack1.pop()
                else:
                    stack2.append(i)
            res.append(s1)
        
        # 去除 不合理 的 '('
        for i in stack1:
            res[i] = ''
         # 去除 不合理 的 ')'
        for i in stack2:
            res[i] = ''
        
        return ''.join(res)