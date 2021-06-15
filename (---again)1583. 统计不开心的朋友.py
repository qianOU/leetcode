class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # 使用一个 n*n 的数组来 转换 preferences 的 亲近程度 table
        # pref[i][j] 表示的是 j 在 i 的好友中亲密程度的排名
        pref = [[0]*n for i in range(n)]

        for i in range(n):
            for idx, j in enumerate(preferences[i]):
                pref[i][j] = idx
        
        # 邻近表
        adj = [0]*n # 表示的是配对关系
        for i, j in enumerate(pairs):
            adj[i] = j
            adj[j] = i
        
        ans = 0
        for x in range(n):
            y = adj[x] # x 与 y 相连接
            thr = pref[x][y] # 表示 y 在 x 好友中的排名
            for idx in range(thr):
                u = preferences[x][u] # 表示 u 与 x 更亲密的对象
                v = adj[u]
                if pref[u][x] < pref[u][v]:
                    ans += 1 # x 是找到的不开心的朋友
                    break # 一定要break，因为对于 x 的计数，只需要计算一次
        
        return ans
