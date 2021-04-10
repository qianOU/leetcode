class Solution:
    def findComplement(self, num: int) -> int:
        import math
        n = math.ceil(math.log2(num+1))
        # print(n)
        return num ^ (2**n-1)
print(Solution().findComplement(1))