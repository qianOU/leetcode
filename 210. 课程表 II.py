class Solution:
    # 方法1： BFS
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        indegree = [0] * n
        adj = [[] for i in range(n)]

        for cur, pre in prerequisites:
            indegree[cur] += 1
            adj[pre].append(cur)
        
        from collections import deque
        q = deque()

        for i in range(n):
            if not indegree[i]:
                q.append(i)
        
        ans = []
        while q:
            cur = q.popleft()
            ans.append(cur)
            n -= 1
            for j in adj[cur]:
                indegree[j] -= 1
                if not indegree[j]: q.append(j)
        
        return ans if not n else []
    
    # 方法2： DFS
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        adj = [[] for i in range(n)]
        status = [0] * n

        for cur, pre in prerequisites:
            adj[pre].append(cur)
        
        def dfs(i):
            if status[i] == 1: return False
            if status[i] == -1: return True
            status[i] = 1

            for j in adj[i]:
                if not dfs(j): return False
            
            ans.append(i)
            status[i] = -1
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        
        # 由于递归实际上是栈， 所以这里需要反转一下序列
        return ans[::-1]