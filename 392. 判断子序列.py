class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 使用堆栈
        stack = list(t[::-1])
        p = 0
        while stack:
            if s[p] == stack.pop():
                p += 1
            # stack.pop()
        return p == len(s)