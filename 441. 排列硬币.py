class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(-.5+(1+8*n)**.5/2) # 求根公式