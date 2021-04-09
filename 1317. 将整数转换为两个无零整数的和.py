class Solution:
    def getNoZeroIntegers(self, n: int):

        set_a = set(i for i in range(1, n) if i%10)
        print(set_a)
        for i in set_a:
            if n-i in set_a:
                return [i, n-i]

print(Solution().getNoZeroIntegers(11))