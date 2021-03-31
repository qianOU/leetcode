class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        map_ = dict(zip( [chr(i) for i in range(65, 91)], range(1, 27)))
        sum_ = 0
        count = 0
        for i in columnTitle[::-1]:
            sum_ += 26**count*map_[i]
            count += 1
        return sum_
    
A = Solution()
print(A.titleToNumber("ZY"))
