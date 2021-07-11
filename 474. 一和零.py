class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        from collections import deque
        q = deque()
        