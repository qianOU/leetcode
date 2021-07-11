class Solution:
    # 思路1: 二分查询 + 快速乘法
    def divide(self, dividend: int, divisor: int) -> int:
        # 判别符号位，使用了 异或 巧妙！！！
        sign = 1 if divisor ^  dividend < 0  else -1
        # 由于 python 中整除是向 负无穷 取整，为了 保持和其它语言 一致 向 0 取整， 我们对乘数转换为整数，之后再看符号位
        dividend, divisor = abs(dividend), abs(divisor)

        # 快速乘法
        def mul(a, b):
            ans = 0
            while b > 0:
                if b & 1:
                    ans += a
                a <<= 1
                b >>= 1
            return ans
        
        #  要找的值 x,最后 x*divisor 一定是 满足 小于等于 dividend 的第一个数
        l, r = 0, dividend
        while l <= r:
            mid = (l + r) >> 1
            if mul(mid, divisor) <= dividend:
                l = mid + 1
            else:
                r = mid - 1
        
        ans = r if sign > 0 else -r
        return ans if -2**31 <= ans < 2**31 else 2**31 - 1


    # 思路2: 递归 + 倍增 [参考大佬思路]
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if divisor ^ dividend < 0 else 1
        # 由于 python 中整除是向 负无穷 取整，为了 保持和其它语言 一致 向 0 取整， 我们对乘数转换为整数，之后再看符号位
        dividend, divisor = abs(dividend), abs(divisor)

        def dfs(a, b):
            if a < b: return 0
            count = 1
            res = b
            # 退出循环的标志就是， res 是满足 小于等于 a 的最大倍增数
            while (res << 1) <= a:
                count <<= 1
                res <<= 1
            return count + dfs(a - res, b)
        
        item  =  dfs(dividend, divisor)
        item = item if sign > 0 else -item
        
        return  item if -2147483648 <=  item < 2147483648 else 2147483647