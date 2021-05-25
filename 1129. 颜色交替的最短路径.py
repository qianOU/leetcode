class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges, blue_edges):
        adj = [[] for i in range(n)]
        visited = set()
        ans = [-1]*n
        ans[0] = 0

        for i, j in  red_edges:
            adj[i].append((j, 'r'))

        for i, j in  blue_edges:
            adj[i].append((j, 'b'))

        print(adj)
        from collections import deque
        q = deque()
        q.append((-1,0, None))

        count = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                prev, cur, color = q.popleft()
                print(prev, cur, color)
                if ans[cur] < 0:
                    ans[cur] = count
                
                for j in adj[cur]:
                    print(cur, j)
                    if j[-1] != color and (cur, *j) not in visited:
                        visited.add((cur, *j))
                        q.append((cur, *j))
            
            count += 1
        
        return ans


print(Solution().shortestAlternatingPaths(n = 3, red_edges = [[0,1],[1,2]], blue_edges = []))