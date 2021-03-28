class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        
        if len(strs) == 1:
            return strs[0]

        left = 0
        short = min(len(i) for i in strs)

        if short == 0:
            return ''

        while True:
            head = strs[0][left]
            for string in strs[1:]:
                if string[left] != head:
                    return strs[0][:left]
            
            left += 1
        
            if left == short:
                return strs[0][:short]
A = Solution()
print(A.longestCommonPrefix(["dog","dogecar","dogcar"]))
            