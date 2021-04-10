class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        import re
        return bool(re.search(r'^(\w+)\1+$', 'aba'))