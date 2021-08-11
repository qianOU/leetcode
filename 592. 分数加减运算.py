class Solution:
    def fractionAddition(self, expression: str) -> str:
        # 辗转相处法
        def gcd(a, b):
            if a % b == 0: return b
            return gcd(b, a % b)
        
        def get_simple(a, b):
            if a == 0: return [0, 1]
            if a >= b:
                factor = gcd(a, b)
            else:
                factor = gcd(b, a)
            if factor == 1: return [a, b]
            return get_simple(a // factor, b // factor)


        stack = []
        sign = -1 if  expression[0] == '-' else 1
        right, item = False, 0
        n, one = len(expression), [0, 1]
        stack.append(one.copy())
    
        for idx in range(n + 1):
            if idx < n and expression[idx].isdigit():
                item = item * 10 + int(expression[idx])
            elif idx < n and expression[idx] == '/':
                one[0] = sign * item
                item = 0
            else: 
                one[1] = item
                num, den = stack.pop()
                top = num * one[1] + one[0] * den
                flag = 1 if top >= 0 else -1
                tmp = get_simple(abs(top), den*one[1])
                tmp[0] *= flag
                stack.append(tmp)
                sign = -1 if idx < n and expression[idx] == '-' else 1
                item = 0

        return '{0}/{1}'.format(*tmp)

print(Solution().fractionAddition("5/3+1/3"))


