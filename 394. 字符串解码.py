class Solution:
    def decodeString(self, s: str) -> str:
        time = [] # 存放需要匹配次数的栈
        stack = [] # 存放扫描结果的栈
        for i in s:
            if i == ']':
                tmp = ''
                while stack and stack[-1] != '[':
                    tmp = stack.pop() + tmp
                stack.pop() # 弹出 [
                
                #按指定次数重复入栈
                repeates = time.pop()
                for i in range(int(repeates)):
                    stack.append(tmp)

            else:
                if i == '[':
                    times = ''
                    while stack and stack[-1].isdigit():
                        times = stack.pop() + times
                
                    time.append(times)

                stack.append(i)
        
        return ''.join(stack)