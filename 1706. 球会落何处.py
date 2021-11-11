from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [-1]*n
        q = list((i, i) for i in range(n))
        for row in grid:
            tmp = [] # 一定是相对有序的，所以使用list即可，不用有序结构
            print(q)
            for i in range(len(q)):
                cur, idx = q[i]
                if i and tmp and row[cur] - row[q[i-1][0]] == -2: # V字形的情况
                    tmp.pop()
                    continue
                if 0 <= cur + row[cur] < n: 
                    tmp.append((cur + row[cur], idx))
            q = tmp

        
        for i, j in tmp:
            ans[j] = i
        return ans

print(Solution().findBall(
[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
))