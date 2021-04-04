class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        n = len(s)
        ans = ''
        for i in range(n-1):
            for j in range(i+2, n+1):
                total = set(s[i:j])
                for ch in total:
                    if ch.swapcase() not in total:
                        break
                if j-i > len(ans):
                    ans = s[i:j]
        return ans

                     
A = Solution()
print(A.longestNiceSubstring("cChH"))      
