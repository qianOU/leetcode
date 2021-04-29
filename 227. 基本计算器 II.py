class Solution:
    # 写的复杂了，实际上可以将 + 与 - 视为数字符号先压入栈，再查看数字前面的的符号如果是 乘或者 除先与栈顶数字做运算再入栈
    def calculate(self, s: str) -> int:
        import collections
        nums =collections.deque()
        opr = collections.deque()
        s = s + '$'
        n = len(s)
        i = 0
        ans = ''
        while i < n:
            s1 = s[i]
            if s1 == ' ': # 空格
                i += 1
                continue

            elif s1.isdigit():
                ans += s1
                i += 1
                continue
            else:
                if ans:
                    nums.append(int(ans))
                    ans = ''
                if opr and nums and opr[-1] in ('/', '*'):
                    item1 = nums.pop()
                    item2 = nums.pop()
                    if opr[-1] == '/':
                        nums.append(item2 // item1)
                    elif opr[-1] == '*':
                        nums.append(item2 * item1)
                    opr.pop()
                    continue
                if s1 != '$':
                    opr.append(s1)

                i += 1
        # print(opr, nums)
        while opr:
            op = opr.popleft()
            item1 = nums.popleft()
            item2 = nums.popleft()
            if op == '+':
                nums.appendleft(item2 + item1)
            else:
                nums.appendleft(item1 - item2)

        return nums.pop()

    # 优雅写法：
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        n = len(s)
        print(n)
        preSign = '+' #假设第一数子的符号为 ‘+’
        for i in range(n):
            s1 = s[i]
             
            if s1 != ' ' and s1.isdigit():
                num = num *10 + int(s1)
            
            if i == n-1 or s1 in '+-*/': # 当扫描到符号时
                if preSign == '+':
                    stack.append(num)
                if preSign == '-':
                    stack.append(-1*num)
                if preSign == '*':
                    stack[-1] *= num
                if preSign == '/':
                    stack[-1] //= num

                num = 0
                preSign = s1 # 更新符号状态

        print(stack)
        return sum(stack)

print(Solution().calculate("1+1-1"))