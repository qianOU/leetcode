class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 9: return 1

        import math
        k = int(math.log10(n)) + 1 # 位数
        left = n // 10**(k - 1) + 1
        right = 10**(k - 1)
        dp = [0]*(1 + k) # 第 i 位出现 1 的次数
        # base-case
        dp[k] = n % 10**(k-1) + 1 + (right if n // 10**(k - 1) > 1 else 0) 

        print(k, dp[k], left, right)
        for i in range(k-1, 0, -1):

            l, r = k - i, i-1 # 比 i 位高的位数, 比 i 位低的位数
            right //= 10
            dp[i] =  left * right
            left *= 10 

        print(dp) 
        return sum(dp)

print(Solution().countDigitOne(20))