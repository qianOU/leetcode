class Solution:
    def tictactoe(self, board) -> str:
        n = len(board)
        # 查看行是否有获胜的情况
        
        cols = [board[0][i] for i in range(n)]
        diag = [board[0][0], board[0][n-1]]
        flag = 0
        for i in range(n):
            rows = board[i][0]
            for j in range(n):
                if board[i][j] == ' ':

                    flag = 1
                # 行向量
                if  rows != board[i][j]:
                    rows = None
               
                # 列向量
                if board[i][j] != cols[j]:
                    cols[j] = None
            
            # print(rows, cols, diag)
            # 如果 i 行有获胜者
            if rows and rows != ' ':
                return rows   
            # 主对角线
            if board[i][i] != diag[0]:
                diag[0] = None
            # 副对角线
            if board[i][n-1-i] != diag[-1]:
                diag[-1] = None
        
        
        # print(cols, diag, flag)
        import itertools
        for i in itertools.chain(cols, diag):
            if i is not None and i != ' ':
                return i
        

        if flag: 
            return "Pending"
        
        return 'Draw'


print(Solution().tictactoe(
[" OOO","    ","OXXX","XX O"]))
        



                