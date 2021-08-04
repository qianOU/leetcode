class Solution:
    # 思路1：分治
    def generateParenthesis(self, n: int):
        from functools import lru_cache

        @lru_cache(None)
        def dfs(m): # m 个括号有哪些生成方式, 使用集合去重
            if m <= 0 or m > n: return ['']
            res = []
            for i in range(1, 1 + m):
                left = dfs(i-1)
                right = dfs(m-i)
                for l in left:
                    for r in right:
                        res.extend([
                            '(' + l + ')' + r,
                            '('+ l + r + ')',
                            l + '()' + r ,
                            l + '(' + r + ')' ,
                        ])
            
            return set(res)
        
        return dfs(n)
    
    # 思路2. 使用回溯思路
    def generateParenthesis(self, n: int):
        res = []
        # l 代表了剩余左括号的数量， r代表了剩余右括号的数量， 在合法的生成过程中一定有 r >= l
        def dfs(l, r, path): 
            if l > r or l < 0: return 
            elif l == r == 0:
                res.append(''.join(path))
            
            # 做选择填写左括号或者是右括号
            path.append('(')
            dfs(l-1, r, path)
            path.pop()
            path.append(')')
            dfs(l, r-1, path)
            path.pop()
        
        dfs(n, n, [])

        return res


print(Solution().generateParenthesis(3))

