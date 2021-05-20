class Solution:
    def updateBoard(self, board, click) :
        d = [(0, 1), (0, -1), (1, 0), (-1, 0), (1,1), (1, -1), (-1, 1), (-1, -1)]
        m, n = len(board), len(board[0])
        check = lambda x, y:  0<=x<m and  0<=y<n
        isB = lambda x, y: all(board[x+i][y+j] != 'M' for i, j in d if check(x+i, y+j))
        
        visited = set() # 记录已经走过的路径
        def dfs(i, j, step, board):
            if not check(i, j):
                return

            visited.add((i, j))
            if not step and board[i][j] == 'M':
                board[i][j] = 'X'
                return

            if isB(i, j) and board[i][j] == 'E':
                board[i][j] = 'B'

            # flag 确定是否 board[i][j] 需要更新 地雷数量， 如果一开始就反应了地雷状态，则无需再次更新
            flag = 0 if board[i][j].isdigit() else 1

            for l, r in d:
                if flag and check(i+l, j+r) and board[i+l][j+r] == 'M': # 如果board[i][j] 最开始不是数字。并且周围有地雷时 则更新其状态
                    board[i][j] = str(int(board[i][j]) + 1) if board[i][j].isdigit() else '1'
                
                if (i+l, j+r) not in visited and board[i][j] == 'B': # 只有 当前处于周围没有地雷时，才会进行递归
                    dfs(i+l, j+r, step+1, board)

        dfs(click[0], click[1], 0, board)
    
        return board
item = [["B","B","B","B","1","M","M","E"],["B","B","B","B","1","4","M","E"],["B","B","B","B","B","3","M","E"],["B","B","B","B","B","2","M","E"],["1","2","2","1","B","1","1","1"],["E","M","M","1","B","B","B","B"],["E","E","E","2","2","2","2","1"],["E","E","E","E","M","M","E","M"]]


print(Solution().updateBoard(item,
[7,2 ]))

print([["B","B","B","B","1","M","M","E"],["B","B","B","B","1","4","M","E"],["B","B","B","B","B","3","M","E"],["B","B","B","B","B","2","M","E"],["1","2","2","1","B","1","1","1"],["E","M","M","1","B","B","B","B"],["1","2","2","2","2","2","2","1"],["B","B","B","1","M","M","E","M"]])