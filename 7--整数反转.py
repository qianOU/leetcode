class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INTMAX = 2**31 - 1
        INTMIN = - 2**31

        t = 0
        flag = -1 if x < 0 else 1
        x *= flag
    
        while x != 0:
    
            t*=10

            end = x % 10
            x = x // 10

            t += end
        t *= flag
        if t < INTMIN or t > INTMAX:
            return 0
        
        return t


A = Solution()
print(A.reverse(-130))