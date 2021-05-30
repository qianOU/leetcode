class Solution:
    def totalMoney(self, n: int) -> int:
        rund, day = divmod(n, 7)
        return sum((2*i+6)*7//2 for i in range(1, rund+1)) + (rund+1)*day + sum(range(day))
