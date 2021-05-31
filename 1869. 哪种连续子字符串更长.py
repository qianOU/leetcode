class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        len_1 = len_0 = 0
        one = two = 0
        for i in s:
            if i=='1':
                len_0 = max(len_0, two)
                two = 0
                one += 1
            else:
                len_1 = max(len_1, one)
                two += 1
                one = 0
        
        len_1 = max(len_1, one)
        len_0 = max(len_0, two)
        return len_1 > len_0