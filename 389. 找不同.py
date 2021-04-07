class Solution:
    # 散列表
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        a = Counter(t)
        b = Counter(s)
        return (b-a).popitems()[0]

    # 位运算
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for i in s:
            res ^= ord(i)
        
        for j in t:
            res ^= ord(j)
        
        return chr(res)