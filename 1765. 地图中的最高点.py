class Solution:
    # 基础的 BFS 
    def highestPeak(self, isWater):
        d = [(1, 0), (-1, 0), (0, 1), (0,-1)]
        m, n = len(isWater), len(isWater[0])
        check = lambda x, y: 0<=x<m and 0<=y<n
        
        
        from collections import deque
        q = deque()

        ans = []
        for i in range(m):
            tmp = []
            for j in range(n):
                if isWater[i][j]:
                    q.append((i, j))
                    tmp.append(0)
                    continue

                tmp.append(None)
            ans.append(tmp)

        # 其实不需要做判断，只要从多个水域遇见陆地都增加 1， 是能保证 最后 每一个格点高度差是小于 等于1的， 这可以由 BFS 每次都同步递增保证   
        valid = lambda x, y: all(abs(ans[x+i][y+j]-ans[x][y]) <=1 for i,j in d if check(x+i, y+j) and ans[x+i][y+j])
        while q:
            sz = len(q)
            for _ in range(sz):
                x, y = q.popleft()
                for i, j in d: 
                    if check(x+i, y+j):
                        if isWater[x+i][y+j]:
                            ans[x+i][y+j] = 0
                        
                        if not isWater[x+i][y+j] and not ans[x+i][y+j]:
                            ans[x+i][y+j] = ans[x][y] + 1
                            if valid(x+i, y+j):
                                q.append((x+i, y+j))
                                continue
                            ans[x+i][y+j] = ans[x][y]
                            if valid(x+i, y+j):
                                q.append((x+i, y+j))
                                continue
                            ans[x+i][y+j] = ans[x][y] - 1 if ans[x][y] else 0
                            if valid(x+i, y+j):
                                q.append((x+i, y+j))

        return ans


 # 优化的 多远 BFS 
    def highestPeak(self, isWater):
        d = [(1, 0), (-1, 0), (0, 1), (0,-1)]
        m, n = len(isWater), len(isWater[0])
        check = lambda x, y: 0<=x<m and 0<=y<n
        
        
        from collections import deque
        import copy

        q = deque()

        ans = []
        for i in range(m):
            tmp = []
            for j in range(n):
                if isWater[i][j]:
                    q.append((i, j))
                    tmp.append(0)
                    continue
                tmp.append(None)
            ans.append(tmp)
        
        print(ans, q)
        while q:
            x, y = q.popleft()
            for i, j in d: 
                # 未遍历过的节点入队列
                if check(x+i, y+j) and ans[x+i][y+j] is None:
                    # 统一测率，对于陆地部分都做 + 1， 水域保持为 0 
                    ans[x+i][y+j] = ans[x][y] + 1 if not isWater[x+i][y+j] else 0
                    q.append((x+i, y+j))
        
        return ans
         
print(Solution().highestPeak([[0,0,1],[1,0,0],[0,0,0]]))

