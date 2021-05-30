class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        n = numBottles # n瓶酒
        count = 0
        res = 0
        while n:
            count += n
            n, res = divmod(n+res, numExchange)
        return count