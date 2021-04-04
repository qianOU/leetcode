class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l1 = l2 = 0
        n1 = len(word1)
        n2 = len(word2)
        s = ""
        while l1 != n1 and l2!=n2:
            s += word1[l1]
            s += word2[l2]
            l1 += 1
            l2 += 1
        
        return s + word1[l1:n] + word2[l2:n2]