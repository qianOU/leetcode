class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x) #空间复杂度较高
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    # 优化算法
    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x%10==0 and x!=0):
            return False
        
        res = 0
        while res < x:
            res = res*10 + x%10
            x = x//10
        
        return res == x or res%10 == x


A = Solution()
print(A.isPalindrome2(-101))