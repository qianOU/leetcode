class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        from collections import OrderedDict
        a = OrderedDict()
        res = set()
        for i in range(len(s)):
            ch = s[i]
            if ch in res:
                continue
            a[ch] = a.get(ch, []) + [i]
            temp = len(a[ch])
            if temp >= 2:
                res.add(ch)
                del a[ch]
        return next(iter(a.values()))[0] if len(a.values()) else -1