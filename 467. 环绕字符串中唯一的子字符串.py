class Solution:
    # 滑动窗口
    def findSubstringInWraproundString(self, p: str) -> int:
        ans, l, n = 0, 0, len(p)
        record = [0]*26 # record[i] 记录的是 以 p[chr(97 + i)] 为首的环绕字符串的最长长度
        for r in range(1, n+1):
            # 不满足的情况
            if r == n or not (ord(p[r]) - ord(p[r-1]) == 1 or (p[r-1] == 'z' and p[r] == 'a')):
                m = r - l
                base = ord(p[l]) - 97
                for i in range(min(m, 26)):
                    if m - i > record[(base + i) % 26]:
                        ans += m - i - record[(base + i) % 26]
                        record[(base + i) % 26] = m - i
                l = r # 收缩左边界

        return ans

print(Solution().findSubstringInWraproundString("abcdefgefgzazzaabbaazzaaa"))