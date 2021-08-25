class Solution:
    # BFS 超时(因为每次只是增加一个单位)
    def countPaths(self, n: int, roads) -> int:
        base = 10**9 + 7
        time = [float('inf')]*n
        count = [0]*n
        count[0] = 1
        time[0] = 0

        # 邻接表
        adj = [[] for i in range(n)]
        for i, j, c in roads:
            adj[i].append((j, c))
            adj[j].append((i, c))

        from collections import deque
        q = deque([(0, 0)])
        while q:
            cur, cost = q.popleft()
            if cost > time[cur]: continue
            for nxt, c in adj[cur]:
                if time[nxt] >= c + time[cur]:
                    if time[nxt] == c + time[cur]:
                        count[nxt] += 1
                        count[nxt] %= base
                    else: 
                        count[nxt] = 1
                    time[nxt] = c + time[cur]
                    q.append((nxt, c + time[cur]))

        return count[n-1]
    
    # 方法2： DiJstra方法（每次增加的是当前节点的所有最少花费方案）
    def countPaths(self, n: int, roads) -> int:
        from queue import PriorityQueue as PQ
        base = 10**9 + 7
        time = [float('inf')]*n
        count = [0]*n
        count[0] = 1
        time[0] = 0

        # 邻接表
        adj = [[] for i in range(n)]
        for i, j, c in roads:
            adj[i].append((j, c))
            adj[j].append((i, c))
        
        q = PQ()
        q.put((0, 0))
        while not q.empty():
            cost, cur = q.get()
            if cost > time[cur]: continue
            for nxt, c in adj[cur]:
                if c + cost < time[nxt]:
                    time[nxt] = c + cost
                    count[nxt] = count[cur]  # 从 cur --> nxt 是到达 nxt 的最少花费方案
                    q.put((time[nxt], nxt))
                elif c + cost == time[nxt]: # 叠加方案
                    count[nxt] = (count[nxt] + count[cur]) % base
        
        return count[n-1]


print(Solution().countPaths(
12,
[[1,0,2348],[2,1,2852],[2,0,5200],[3,1,12480],[2,3,9628],[4,3,7367],[4,0,22195],[5,4,5668],[1,5,25515],[0,5,27863],[6,5,836],[6,0,28699],[2,6,23499],[6,3,13871],[1,6,26351],[5,7,6229],[2,7,28892],[1,7,31744],[3,7,19264],[6,7,5393],[2,8,31998],[8,7,3106],[3,8,22370],[8,4,15003],[8,6,8499],[8,5,9335],[8,9,5258],[9,2,37256],[3,9,27628],[7,9,8364],[1,9,40108],[9,5,14593],[2,10,45922],[5,10,23259],[9,10,8666],[10,0,51122],[10,3,36294],[10,4,28927],[11,4,25190],[11,9,4929],[11,8,10187],[11,6,18686],[2,11,42185],[11,3,32557],[1,11,45037]]
))