class Solution:
    # 典序的 有向图 是否存在环路的判断
    # 因为课程具有前导性，因此是有向图
    # 解法 一 : BFS
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        n =  numCourses
        indegree = [0] * n
        adj = [[] for i in range(n)]
        q = []
        
        for cur, pre in prerequisites:
            adj[pre].append(cur)
            indegree[cur] += 1

        # 将入度为 0 的节点入队列
        for i in range(n):
            if not indegree[i]:
                q.append(i)
        
        while q:
            cur = q.pop(0)
            n -= 1 # cur 节点 已经被遍历过，所以 总节点数 - 1
            for i in adj[cur]:
                indegree[i] -= 1 # cur -> i 的路径已经遍历过，所以 i 的入度减一
                if not indegree[i]: # 如果 i 的入度 已经为 0， 也就表示其是 下一阶段的搜索目标
                    q.append(i)

        return not n

    # 解法 二 : DFS
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        n = numCourses
        adj = [[] for i in range(n)] #邻接表
        # 0 表示没遍历过的节点， 1 表示被当次 DFS 遍历过的节点， -1 表示 被其它节点遍历过的 节点
        status = [0 for i in range(n)] # 状态表
        for cur, pre in prerequisites:
            adj[pre].append(cur)

        def dfs(i): # 以 i 为搜索起点的 路径不存在环
            if status[i] == -1: return True
            if status[i] == 1: return False

            status[i] = 1 # i 已经在当次被遍历 状态置为 1
            for j in adj[i]:
                if not dfs(j):
                    return False

            status[i] = -1 # 如果 i 的搜索路径中不存在 环， 改边状态，防止重复搜索
            return True
        
        for i in range(n):
            if not dfs(i):
                return False
        
        return True

