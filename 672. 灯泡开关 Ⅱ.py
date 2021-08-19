class Solution:
    # 偶数次还原特性 暴力解法
    def flipLights(self, n: int, presses: int) -> int:
        from functools import lru_cache

        if n == 1: 
            choices = [(1, 0, 0), (0, 0, 0)]
        else: # 第三种方案失去作用
            choices = [(1, 1, 0), (1, 0, 0), (0, 1, 0), (0, 0, int(n > 2))]

      
        visited = set()
        @lru_cache(None)
        def dfs(odd, even, exp, step=0):
            if step == presses:
                visited.add((odd, even, exp))
                return 

            for choice in choices:
                i, j, k = choice
                dfs((odd+i)%2, (even+j)%2, (exp+k)%2, step + 1)
        
        dfs(1, 1, 0, 0)
        print(visited)
        return len(visited)



print(Solution().flipLights(2, 1))