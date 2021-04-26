class Solution:
    # 方法一:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [] # 存放 扫描 符号的栈
        score = [] # 存放得分的栈, 元组(分数, 右括号的索引)
        n = len(S)
        p = 0
        while p < n:
            s1 = S[p]
            if s1 == ')':
                top = stack.pop()
                if p - top == 1: # 只考虑 () 这种情况 
                    score.append((1,p)) 
                else: # 处理 非单 () 的情况
                    total = 0
                    # 在同一个大括号外侧,需要做累加操作 (()...())
                    while  score and top < score[-1][-1] < p:
                        total += score.pop()[0]
                    score.append((total*2, p)) # 最后乘以 2 
                    
            else:
                stack.append(p)

            p+=1
        
        return sum(i[0] for i in score) # 汇总表达式
        

        # 方法二: 优雅,简洁!!!
        def scoreOfParentheses(self, S: str) -> int:
            # 用一个栈来维护当前所在的深度，以及每一层深度的得分。
            stack = [0] # 存放当前层的 分数

            for i in S:
                if i == '(': # 新一层, 
                    stack.append(0) #深度 +1, 该深度的分树初始化为 0
                else:
                    item = stack.pop() # 深度减一
                    stack[-1] += max(2*item, 1) #更新上一层的分数

            return stack.pop()



                

