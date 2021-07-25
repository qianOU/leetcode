class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        m = len(str(n))
        from collections import deque
        q = deque()
