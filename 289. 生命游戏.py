class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def check(i, j):
            count = 0
            for r in (1, -1, 0):
                for c in (1, -1, 0):
                    if r or c:
                        x, y = i+r, c+j
                        if 0<=x<m and 0<=y<n and board[x][y]:
                            # print(x, y, count)
                            count += 1
            print(i,j, count)
            if count == 3:
                board[i][j] = 1
                return 
            elif count == 2 and board[i][j]:
                return 
            else:
                board[i][j] = 0
            
        check(1, 0)
        for i in range(m):
            for j in range(n):
                check(i, j)

        return board

print(Solution().gameOfLife(
[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))