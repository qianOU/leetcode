class Solution:
    # 方法1： BFS
    def minimumEffortPath(self, heights) -> int:
        m, n = len(heights), len(heights[0])
        d = [(0, 1),  (1, 0), (-1, 0), (1, 0)]
        check = lambda x, y: 0<=x<m and 0<=y<n
        
        from collections import deque
        q = deque([(0, 0, 0)])
        
        ans = float('inf')
        while q:
            x, y, v = q.popleft()
            prev = heights[x][y]
            if (x, y) == (m-1, n-1):  
                ans = min(ans, max(v, abs(heights[m-1][n-1]-prev)))
                continue
            for i, j in d:
                if check(x+i, y+j):
                    now = heights[x+i][y+j]
                    v1 = max(v, abs(now - prev))
                    q.append((x+i, y+j, v1))
        
        return ans

print(Solution().minimumEffortPath(
[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))