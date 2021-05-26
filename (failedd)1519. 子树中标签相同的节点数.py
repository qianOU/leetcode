class Solution:
    # 树的根节点是 0 BFS
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        n = len(labels)
        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(i)
            adj[j].append(j)
        
        # 真正的上下级关系
        true_pair =  [[] for _ in range(n)]
        visited = set()
        visited.add(0)
        from collections import deque
        q = deque()
        q.add((0, -1))

        while q:
            sz = len(q)
            for _ in range(sz):
                prev, cur = q.popleft()
                if prev>=0: true_pair[prev].append(cur)
                for j in adj[cur]:
                    if j not in visited:
                        visited.add(j)
                        q.append((cur, j))



        print(true_pair, q)
        ans = [dict.fromkeys(labels, 0) for _ in range(n)]
        
        visited.clear()
        adj = [[] for _ in range(n)]
        res = [0]*n
        # 拓扑排序
        for i in range(n):
            if not true_pair[i]:
                q.append(i)
                visited.add(i)
            else:
                for j in true_pair[i]:
                    adj[j].append(i)
        
        selections = set(labels)
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                ans[cur][labels[cur]] += 1
                for i in true_pair:
                    for p in selections:
                        ans[cur][p] += ans[i][p]
                
                res[cur] += ans[cur][labels[cur]]
                for j in adj[cur]:
                    if j not in visited:
                        q.append(j)


        return res
        


        