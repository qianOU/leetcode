class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        stack = []
        mc = 0
        count = 0
        for i in hours:
            if i > 8:
               mc += 1
            elif mc > 0:
                mc -= 1
            else:
                mc = 0
            
            count = max(count, mc)
        
        return count