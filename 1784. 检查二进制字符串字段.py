class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return '01' not in s
print(Solution().checkOnesSegment('101100'))