class Solution:
    # 使用指针进行扫描
    def wordPattern(self, pattern: str, s: str) -> bool:
        l2 = p1 = p2 = 0
        records = dict()
        n2 = len(s)
        n1 = len(pattern)
        while p2 < n2:
            if s[p2] == ' ':
                if p1>=n1 or (records.get(pattern[p1], None) is None and s[l2:p2] in records.values()) or(records.get(pattern[p1], None) is not None and records[pattern[p1]] != s[l2:p2]):
                    return False
                records[pattern[p1]] = s[l2:p2]
                l2 = p2+1
                p1 += 1
            p2 += 1
        # 最后一个单词作比较
        # print(p1, n1, l2, p2, records)
        if p1>=n1 or (records.get(pattern[p1], None) is None and s[l2:p2] in records.values()) or(records.get(pattern[p1], None) is not None and records[pattern[p1]] != s[l2:p2]):
            return False
        return p1 == n1-1

    # 使用python技巧
    def wordPattern(self, pattern: str, s: str) -> bool:
       if len(pattern.split()) != len(set(s)):
           return False
        # 双射的配对关系可以使用集合中的配对元组来唯一表示 不妨设为 集合 A
        # 集合 A 的长度 与 集合B,C的长度一致。就说明没有冲突现象存在 
        if len(zip(pattern, s.split())) == len(set(pattern.split())) == len(set(s)):
            return True
        return False 

A =Solution()
print(A.wordPattern("abba",
"dog dog dog dog"))