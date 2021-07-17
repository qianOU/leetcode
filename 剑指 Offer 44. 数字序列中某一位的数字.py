class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9: return n

        n -= 9        
        res = 0
        weight, x = 2, 90
        while res + weight*x < n:
            res += weight*x
            weight += 1
            x *= 10
        
        delta = n - res
        p, q = divmod(delta, weight)
        print(n, res, weight, x, p, q)
        base = 10**(weight - 1) + p-1
        if not q: return base % 10
        print(base, weight)
        return (base+1) // (10**(weight-q))


print(Solution().findNthDigit(220))