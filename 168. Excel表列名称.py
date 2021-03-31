class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        map_ = dict(zip(range(1, 27), [chr(i) for i in range(65, 91)]))
        ans = ''
        while columnNumber: 
            
            temp = columnNumber % 26
            ans += map_[temp if temp != 0 else 26]
            if temp == 0: # 处理进位情况
                columnNumber -= 26
            columnNumber = columnNumber//26

            
        
        return ans[::-1]

A = Solution()
print(A.convertToTitle(701))