class Solution:
    # 递归的解法,写的不够优雅.忽略了 负数次幂,可以看成 正数次幂的倒数 这一本质
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1

        if n & 1: return (x if n>0 else 1/x) * self.myPow(x, n-1 if n > 0 else n + 1)
        else: return  self.myPow(x, n // 2 if n > 0 else -(-n // 2)) ** 2

    # 优雅的递归写法
    def myPow(self, x: float, n: int) -> float:
        def quickPow(x, n):
            if n == 0: return 1

            if n & 1: # 奇数情况
                return x * quickPow(x, n-1)
            else: # 偶数情况
                return  quickPow(x, n // 2) ** 2

        return quickPow(x, n) if n >= 0 else 1 / quickPow(x, -n)


    # 迭代写法的 快速幂算法
    # 算法主体思想是, n 的二进制表示中, 若 i位为 1, 则 final *= (x)**(z**i), 其中 final是最终的幂结果
    # 同样的只考虑正数,负数次幂就是 取倒数的关系
    def myPow(self, x: float, n: int) -> float: 
        res = 1
        m = abs(n)
        while m:
            if m & 1:
                res *= x
            x *= x
            m >>= 1
        return res if n >= 0 else 1 / res 
