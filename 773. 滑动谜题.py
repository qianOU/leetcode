class Solution:
    # BFS 将二维棋盘直接放进队列中， 效率较低
    # 正确的提高效率的方式是将 二维棋盘压缩成一维，并且直接书写 搜素方向数组 d
    
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m, n = 2, 3
        target = [[1,2,3],[4,5,0]]
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        encode = lambda mat: tuple(sum(mat, []))

        visited = set()
        from collections import deque
        q = deque()

        for i in range(m):
            for j in range(n):
                if not board[i][j]:
                    visited.add(encode(board))
                    q.append((i, j, board))
                    break
        
        import copy
        count = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                x1, y1, bor = q.popleft()
                if bor == target:
                    return count

                for i, j in d:
                    x, y = x1+i, y1+j
                    if check(x, y):
                        mat = copy.deepcopy(bor)
                        mat[x][y], mat[x1][y1] = mat[x1][y1], mat[x][y]
                        item = encode(mat)
                        if item not in visited:
                            visited.add(item)
                            q.append((x,y,mat))
            
            count += 1

        return -1
