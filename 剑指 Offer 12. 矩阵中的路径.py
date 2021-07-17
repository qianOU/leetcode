class Solution:
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])
        length = len(word)
        d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(row, col, cur=0):
            

            if cur == length - 1:
                return True
            
            sign = board[row][col]
            board[row][col] = '' # 当前轮已经遍历过

            for i, j in d:
                x, y = row + i, col + j
                if 0 <= x < m and 0 <= y < n and board[x][y] == word[cur + 1]:
                    if dfs(x, y, cur + 1):
                        return True
            
            board[row][col] = sign # 面对下一轮进行 恢复
        

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    print(i, j, board)
                    if dfs(i, j, 0):
                        return True
        return False
                    
        
print(Solution().exist(
[["C","A","A"],["A","A","A"],["B","C","D"]],
"AAB"))