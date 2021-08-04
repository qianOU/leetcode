class Solution:
    # 思路1： 滑动窗口（枚举窗口的字符类型,使滑动窗口具有二义性）
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        # 枚举窗口的字符类型,使滑动窗口具有二义性
        for i in range(26):
            ch = chr(i + ord('A'))
            res = k
            l = 0
            for r in range(n):
                if s[r] != ch and res >= 0:
                    res -= 1
                # 收缩左边界
                while l <= r and res < 0:
                    if s[l] != ch: res += 1
                    l += 1
                
                ans = max(ans, r - l + 1)
        return ans
    
    # 思路2： 滑动窗口直接维护在小于 k 次替换的时候，包含重复字母的最长子串的长度
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        counter = [0] * 26
        more = l = 0
        for r in range(n):
            idx = ord(s[r]) - ord('A')
            counter[idx] += 1
            if counter[idx] > more: more = counter[idx]
            if r - l + 1 - more > k:  # 如果 [l, r] 中最多的数字次数 需要 k+1 次替换的时候才能形成重复子串，则将左边界 + 1，使得区间长度依然为 r - l 即前面遍历获得的最长重复子串的长度
                counter[ord(s[l]) - ord('A')] -= 1 
                l += 1

        return r - l + 1