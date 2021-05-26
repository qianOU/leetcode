class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n =len(mat), len(mat[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        check = lambda x, y: 0<=x<m and 0<=y<n

        def mark(mat):
            sum_ = 0
            for i, i_v in zip(range(m), [1, 10, 100]):
                for j,j_v in zip(range(n), [1,2,5]):
                        sum_ += mat[i][j]*i_v*j_v
            return sum_

        import copy
        from collections import deque
        q = deque()
        q.append(mat)
        visited = set([mark(mat)])

        count = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                mat = q.popleft()

                if all(i==0 for row in mat for i in row):
                    return count

                for i in range(m):
                    for j in range(n):
                        mat1 = copy.deepcopy(mat)
                        mat1[i][j] = 1 - mat1[i][j]
                        for l,r in d:
                            x, y = i+l, j+r
                            if check(x, y):
                                mat1[x][y] = 1-mat1[x][y]
                        
                        sign = mark(mat1)
                        if sign not in visited:
                            visited.add(sign)
                            q.append(mat1)
            
            count += 1

        return -1


