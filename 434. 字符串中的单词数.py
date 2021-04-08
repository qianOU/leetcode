class Solution:
    def countSegments(self, s: str) -> int:
        return len(re.findall('[^\s]+', s))