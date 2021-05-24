class Solution:
    # 多源 BFS
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        d = [(0,1), (0, -1), (1, 0), (-1, 0)]
        check = lambda x, y: 0<=x<m and 0<=y<n
        dis = [[0]*n for i in range(m)]


        from collections import deque
        q = deque()
        num = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j]: num += 1
                else: q.append((i, j))
        
        count = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                l, r = q.popleft()
                if not num:
                    return dis
                for i,j in d:
                    x, y = l+i, r+j
                    if check(x, y) and not dis[x][y] and mat[x][y]:
                        dis[x][y] = count + 1
                        mat[x][y] = 0 # 已经遍历过
                        q.append((x, y))
                        num -= 1
            count += 1
        return dis

        