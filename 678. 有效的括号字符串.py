# 有效的括号字符串 必修要求左括号数量大于等于右括号数量
class Solution:
    #思路1： 使用记忆化暴力进行递归求解 
    def checkValidString(self, s: str) -> bool:
        @lru_cache(None)
        def dfs(l, r, s):
            if l < r: return False
            if not s: return l == r
            for i in range(len(s)):
                if l < r: return False # 任何子串都要求左括号数量大于等于右括号数目
                if s[i] == '*':
                    return any([dfs(l+1, r, s[i+1:]), dfs(l, r+1, s[i+1:]), dfs(l, r, s[i+1:])])
                l += s[i] == '('
                r += s[i] == ')'
            return l == r

        return dfs(0, 0, s)


print(Solution().checkValidString("(()(()))(()()()))))((((()*()*(())())(()))((*()(*((*(*()))()(())*()()))*)*()))()()(())()(()))())))"))

