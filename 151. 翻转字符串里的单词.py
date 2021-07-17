class Solution:
    # 滑动窗口局部翻转 + 整体翻转
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        l = 0
        # print(s)
        for r in range(n):
            if s[r] == ' ' or r == n-1:
                right = r
                r = r if s[r] != ' ' else r - 1
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                l = right + 1
        
        # print(s, ''.join(s))
        # 取除首位空格
        l, r = 0, n - 1
        while s[l] == ' ' or s[r] == ' ':
            if s[l] == ' ': s[l], l = '', l + 1
            if s[r] == ' ': s[r], r = '', r - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        # print(''.join(s))
        # 处理多余空格
        for i in range(1, n):
            if s[i] == s[i-1] == ' ':
                s[i-1] = ''

    
        return ''.join(s)