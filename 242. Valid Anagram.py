class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        m_s = dict()
        for i in range(len(s)):
            s1, s2 = s[i], t[i]
            if s1 == s2:
                continue
            m_s[s1] = m_s.get(s1, 0) + 1
            m_s[s2] = m_s.get(s2, 0) - 1
        
        return all(i==0 for i in m_s.values())