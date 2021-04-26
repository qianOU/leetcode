class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                one = stack.pop()
                two = stack.pop()
                stack.append(one + two)
            elif i == '/':
                one = stack.pop()
                two = stack.pop()
                stack.append(int(two / one))
            elif i== '-':
                one = stack.pop()
                two = stack.pop()
                stack.append(two - one)
            elif i == '*':
                one = stack.pop()
                two = stack.pop()
                stack.append(one * two)
            else:
                stack.append(int(i))

            print(stack)
        return stack.pop()

print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))