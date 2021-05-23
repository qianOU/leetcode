class Solution:
    # 有向图
    def networkDelayTime(self, times, n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        cost = dict()
        visited = [float('inf')] * (n+1)
        visited[k] = 0


        for i, j, v in times:
            cost[(i, j)] = v
            adj[i].append(j)


        from collections import deque
        q = deque()
        q.append((k, 0))
        print(cost)
        # 用边来避免重复遍历
        while q:
            cur, time = q.popleft()
            # 更新条件是 使得 新节点的 时间缩短了，这样子就有必要更新 新节点 邻近节点的接受时间
            for nex in adj[cur]:
                if cost.get((cur, nex)) + time < visited[nex]: # 如果 使得 nex 所需要的时间变短了，则更新 nex 为源头的其它序列
                    visited[nex] = cost.get((cur, nex)) + time 
                    q.append((nex, time + cost.get((cur, nex))))
                    
        max_time = max(visited[1:])
        return max_time if max_time != float('inf') else -1

print(Solution().networkDelayTime([[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]],
5,
3))
        


