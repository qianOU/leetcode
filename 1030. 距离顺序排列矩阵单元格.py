class Solution:
    # 方法一： BFS
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        from collections import deque

        d = {[0, 1], [0, -1], [1, 0], [-1, 0]} # 方向数组
        q = deque([(r0, c0)])
        visited = set([(r0, c0)])

        ans = []
        while q:
            sz = len(q)
            for _ in range(sz):
                step = q.popleft()
                ans.append(step)
                for i, j in d:
                    new = (step[0] + i, step[-1] + j)
                    if 0 <= new[0] < R and 0<= new[1] < C:
                        if new not in visited:
                            q.append(new)
                        else:
                            visited.add(new)
        
        return ans
                    

    # 方法2: 桶排序 ， 按照曼哈顿距离分桶 
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        maxnum = max(r0, R-1-r0) + max(c0, C-1-c0) # 其中 R, C 是从 1开始计数的
        # 曼哈顿距离的取值范围为 [0, maxnum]
        bucket = [[] for i in range(maxnum+1)]
        dist = lambda r1, c1:abs(r1 - r0) + abs(c1 - c0)
        for i in range(R):
            for j in range(C):
                bucket[dist(i, j)].append([i, j])
        
        ans = []
        for i in range(maxnum+1):
            ans.extend(bucket[i])
        
        return ans

