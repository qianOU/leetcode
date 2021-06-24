class Solution:
    def exist(self, board, word: str) -> bool:
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(word)
        visited = set()
        rows, cols = len(board), len(board[0])
        def dfs(i, j, order):
            if order == n:
                return True
            
            for r, c in d:
                x, y = i+r, j+c
                if 0<=x<rows and 0<=y<cols and board[x][y] == word[order] and (x, y) not in visited:
                    visited.add((x, y))

                    if dfs(x, y, order + 1):
                        return True
                    # 回溯
                    visited.discard((x, y))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(i, j, 1):
                        return True
                    # 回溯
                    visited.discard((i, j))
        
        return False