class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        areas = [set() for i in range(9)]

        flag = True

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rows[i]:
                        flag = False
                        break
                    rows[i].append(board[i][j])
                    
                    if board[i][j] in cols[j]:
                        flag = False
                        break
                    cols[j].append(board[i][j])

                    mask = i//3 * 3 + j//3 
                    if board[i][j] in areas[mask]:
                        flag = False
                        break 
                    areas[mask].append(board[i][j])

            if not flag:
                break

        return flag