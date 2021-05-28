class Solution:
    # 树的根节点是 0 BFS
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        n = len(labels)
        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        visited = [False]*n
        from collections import Counter
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i): # 返回以 i 为更节点的，与label[i] 相同的节点数
            a = Counter(labels[i])
            
            for j in adj[i]:
                if not visited[j]:
                    visited[j] = True
                    b = dfs(i)
                    a += b 

            return a
        
        ans = [0]*n
         
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                p = dfs(i)
                ans[i] = p[labels[i]]
        
        return ans


            