class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        from itertools import zip_longest
        n1, n2 = len(num1), len(num2)
        if n1 > n2:
            num1, num2 = num2, num1 # 确保 num1 是较小的那个值
        sum_ = 0
        p = 0
        for i, j in zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            increase, cur = divmod(int(i)+int(j), 10)
            sum_ +=  cur * 10**p
            print(increase, cur, sum_)
            p += 1
            sum_ += increase*10**p

        return sum_

print(Solution().addStrings('11','123'))