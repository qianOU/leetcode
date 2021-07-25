class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b: return 1
        last = b.pop()
        left = self.pow(self.superPow(a, b), 10)
        right = self.pow(a, last)
        return (right * left) % 1337
        

    # 快速幂运算
    def pow(self, x, k):
        base = 1337
        res = 1
        x %= base
        while k:
            if k & 1:
                res *= x
                res %= base
            x *= x
            x %= base
            k >>= 1
        return res