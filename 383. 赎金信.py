class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        a = Counter(magazine)
        b = Counter(ransomNote)
        return not bool(b-a)