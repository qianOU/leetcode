class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        from functools import reduce
        from operator import xor
        return reduce(xor,[start+2*i for i in range(n)], 0)