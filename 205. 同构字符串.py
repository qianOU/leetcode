class Solution(object):
    # 使用哈希集合
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p1 = 0
        records = set()
        records_s = set()
        records_t = set()
        while p1 != len(s) and p1 != len(t):
            s1, s2 = s[p1], t[p1]
            conditions = [
                (s1, s2) not in records,
                s1 not in records_s,
                s2 not in records_t
            ]
            if all(conditions):
                records.add((s1, s2))
                records_s.add(s1)
                records_t.add(s2)
            elif False in conditions and any(conditions):
                return False
            p1 += 1
        return True

        # 同构 指的是双向映射关系
    def isIsomorphic2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s2t = dict()
        t2s = dict()
        p = 0
        while p < len(s):
            s1 = s[p]
            s2 = t[p]
            # 同构关系是双向的，如果任何一方造成不匹配，就不是同构字符串·
            if (s2t.get(s1, '') and s2t[s1] != s2) or\
                (t2s.get(s2, '') and t2s[s2]!= s1):
                return False
            s2t[s1] = s2
            t2s[s2] = s1
            p += 1
        return True
    

A = Solution()
print(A.isIsomorphic2("paper", 'title'))