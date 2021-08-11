class Solution:
    # 思路：这类题目只能枚举 
    # 状态压缩 + DFS
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal: return True
        if sum(range(1+maxChoosableInteger)) < desiredTotal:return False

        from functools import lru_cache

        @lru_cache(None)
        def dfs(state, cumsum): # state 的第 i 个bit 位，表示的是是否选择 i + 1
            for i in range(1, 1 + maxChoosableInteger):
                if (1 << i-1) & state == 0: # 如果 i 还没被选择
                    # 如果选择 i 能赢，或者 使得下一个人无论如何都赢不了，则表示当前者获胜
                    if cumsum + i >= desiredTotal or not dfs(state | (1 << i-1), cumsum + i):
                        return True
            
            return False # 无论选择任何方案都不可能赢(即一定是输的)
        
        return dfs(0, 0)
