class Solution:
    # 运算表达式的所有可能的结果的变体（分治算法）
    def countEval(self, s: str, result: int) -> int:
        from functools import lru_cache
        from collections import defaultdict
        
        @lru_cache(None)
        def dfs(s): #放回 字符串 s 的所有可能运算结果
            if s in '01': return {int(s): 1}
            n = len(s)
            res = defaultdict(int)
            for i in range(n):
                if s[i] not in '01':
                    left = dfs(s[:i])
                    right = dfs(s[i+1:])
                    for l, v1 in left.items():
                        for r, v2 in right.items():
                            if s[i] == '|': item = l | r
                            elif s[i] == '&': item = l & r
                            elif s[i] == '^': item = l ^ r
                            res[item] += v1*v2
            return res

        q = dfs(s)
        return sum(q[i]  for i in q if i == result)

print(Solution().countEval(
"1&0^1^0|0&0|1^0|0|0&1^0|1|0^1|1",
0
))