class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()

        left = 0
        right = len(s) - 1

        while left <= right:
            s1 = s[left]
            s2 = s[right]
            if not s1.isdigit() and not s1.isalpha():
                left += 1
                continue
            if not s2.isdigit() and not s2.isalpha():
                right -= 1
                continue
            if s1 == s2:
                left += 1
                right -= 1
            else:
                return False
        
        return True