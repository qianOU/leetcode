class Solution:
    def flipChess(self, chessboard) -> int:
        m, n = len(chessboard), len(chessboard[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0),
            (-1, -1), (-1, 1), (1, -1), (1, 1)]

        chessboard2 = chessboard
        chessboard = list(map(list, chessboard2))
        check = lambda x, y: 0 <= x < m and 0 <= y < n

        def search(x, y, d_i, d_j): # 判断x，y 沿着 d_i, d_j 方向是否是一条拓展路径，如果是将路径上的白棋翻转为黑色，其后返回路径上的所有棋子
            if not check(x, y) or chessboard[x][y] == '.': 
                return False, []
            if chessboard[x][y] == 'X': 
                return True, []
            chessboard[x][y] = 'X'
            flag, tmp = search(x + d_i, y + d_j, d_i, d_j)
            if not flag:
                chessboard[x][y] = 'O'
                return False, []
            return flag, [(x, y)] + tmp 
        
        def dfs(x, y):
            count = 0
            for i, j in d:
                x1, y1 = x + i, y + j
                flag, tmp = search(x1, y1, i, j)
                while tmp: 
                    count += 1 + dfs(*tmp.pop())
            return count

        ans = 0
        for i in range(m):
            for j in range(n):
                if chessboard[i][j] == '.':
                    ans = max(ans, dfs(i, j))
                    chessboard = list(map(list, chessboard2)) # 更新棋盘
        return ans