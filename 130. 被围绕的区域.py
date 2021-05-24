class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(board), len(board[-1])
        check = lambda x,y: 0<x<m-1 and 0<y<n-1
        
        visited = set()
        def dfs(i, j):
            count = 0
            for l,r in  d:
                x, y = i+l, r+j
                if check(x, y) and board[x][y] == 'O' and (x, y) not in visited:
                    visited.add((x, y))
                    dfs(x, y)
                if check(x, y) and (board[x][y] == 'X' or (x, y) in visited):
                    count += 1
            
            if count == 4:
                board[i][j] = 'X'
                return 
    
        
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    visited.add((i, j))
                    dfs(i, j)
        
        return board


print(Solution().solve([["O","O","O","O"],["O","O","O","O"],["O","O","O","O"]]))