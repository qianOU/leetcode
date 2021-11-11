
from typing import List
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        adj = [[] for i in range(n)]
        for i, j, c in edges:
            adj[i].append((j, c))
            adj[j].append((i, c))
        
        visit = [False]*n
        visit[0] = True
        self.ans = 0
        def dfs(cur, t, v):
            print(cur, t, v)
            if t >= maxTime:
                return 
            if cur == 0:
                self.ans = max(self.ans, v)
            
            # if all(visit[i[0]] for i in adj[cur]): return 
            for nxt, c in adj[cur]:
                if not visit[nxt]:
                    visit[nxt] = True
                    dfs(nxt, t + c, v + values[nxt])
                    visit[nxt] = False
                else:
                    dfs(nxt, t + c, v)
        
        dfs(0, 0, values[0])
        return self.ans
            

        
        
print(Solution().maximalPathQuality(
[5,10,15,20],
[[0,1,10],[1,2,10],[0,3,10]],
30
))