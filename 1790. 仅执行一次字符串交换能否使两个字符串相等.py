class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        p1 = 0 
        prev = -1

        while p1 != len(s1):
            if s1[p1] != s2[p1]:
                if prev >= 0:
                    print(prev, p1)
                    return s1[prev] == s2[p1] and s2[prev] == s1[p1] and s1[p1+1:] == s2[p1+1:]
            
                prev = p1


            
            p1+=1
        print(prev)
        return True if prev < 0 else False

print(Solution().areAlmostEqual('aa', 'ac'))