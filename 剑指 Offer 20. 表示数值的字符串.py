class Solution:
    # 写的比较混乱
    def isNumber(self, s: str) -> bool:
        stack = []
        s = s.strip() # 去掉首位空格
        n = len(s)
        sign = ''
        res = ''
        has_e = ''
        f = ''
        prev = ''
        for i in range(n):
            ch = s[i]
            if ch == ' ': return False
            if ch in '+-' :
                if sign and s[i-1] not in 'eE' or i==n-1 or (not s[i+1].isdigit() and s[i+1] != '.') or prev.isdigit(): 
                    return False
                sign = ch
            if ch in 'eE':
                if has_e or (not prev.isdigit() and prev != '.') or i==n-1: return False
                has_e  = ch
            if ch == '.':
                if f or has_e or (not prev.isdigit() and (i==n-1 or not s[i+1].isdigit())): return False
                f = '.'
            if ch.isalpha() and ch not in 'eE': return False

            prev = ch
            res += ch
        
  
        return bool(res)

    # 剥离细节
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        n = len(s)
        pos_sign = pos_dot = pos_e = -1
        has_num = False # 是否有数字出现
        for i in range(n):
            ch = s[i]
            # + - 只能在字符串首位，或者 e 的后一位
            if ch in "+-":
                if i == pos_e + 1 and i < n - 1:
                    pos_sign = i
                else: return False
            
            # '.' 只能出现一次, 且如果存在e只能出现在 e 之前 
            if ch == '.':
                if -1 == pos_e and pos_dot < 0 : pos_dot = i
                else: return False
            
            # e/E 只出现一次, 不能出现在首/尾位, 并且 之前一定要有数字出现
            if ch in 'eE':
                if  0 < i < n-1 and pos_e < 0 and has_num: pos_e = i
                else: return False

            # 如果是空格或者 非 e/E 字母，返回 False
            if ch == ' ' or (ch.isalpha() and ch not in 'eE'): 
                return False

            if ch.isdigit():
                has_num = True

        return has_num