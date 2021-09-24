class Solution:
    def flipChess(self, chessboard) -> int:
        m, n = len(chessboard), len(chessboard[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0),
            (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        chessboard = list(map(list, chessboard))
        check = lambda x, y: 0 <= x < m and 0 <= y < n

        def search(x, y, d_i, d_j):
            if not check(x, y) or chessboard[x][y] == '.': 
                return False, []
            if chessboard[x][y] == 'X' and not any('0' in chessboard[x+i][y+j] for i, j in d if check(x+i, y+j)): 
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
        
        return ans

print(Solution().flipChess([".O.....",".O.....","XOO.OOX",".OO.OO.",".XO.OX.","..X.X.."]))