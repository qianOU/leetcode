import pprint
class Solution:
    # 回溯
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def check(i, j, v):
            # 行
            for y in range(n):
                if board[i][y] == v: return False
            
            # 列
            for x in range(m):
                if board[x][j] == v: return False
            
            # 主宫格
            m1, n1 = i // 3, j // 3
            for x in range(3):
                for y in range(3):
                    if board[m1*3 + x][n1*3 + y] == v:
                        return False
            
            return True

        def backtrace(i, j):
            if i == m:
                return True

            while j < n and board[i][j] !=".":
                j += 1
            # print(i, j)
            
            if j < n:
                for v in range(1, 10):
                    # 做选择
                    if check(i, j, str(v)):
                        board[i][j] = str(v)
                        if backtrace(i, j+1): 
                            return True
                        board[i][j] = "."

            if j == n:
                return backtrace(i+1, 0)

        backtrace(0, 0)
        return board
        




pprint.pprint(Solution().solveSudoku(
[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
))