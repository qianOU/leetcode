class Solution:
    def placeWordInCrossword(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])
        length = len(word)
        visited = set()
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(x, y, p, d):
            if p >= length:
                x1, y1 = x + d[0], y + d[1]
                if 0 <= x1 < m and 0 <= y1 < n and board[x1][y1] != '#':
                    return False
                x2, y2 = x - length*d[0], y - length*d[1]
                if 0 <= x2 < m and 0 <= y2 < n and board[x2][y2] != '#':
                    return False
                return True
            print(x,y,p)
            visited.add((x, y, d))
            x1, y1 = x + d[0], y + d[1]
            if 0 <= x1 < m and 0 <= y1 < n and board[x1][y1] != '#' and ((x1 - d[0], y1 - d[1], d) in visited or (x1, y1, d) not in visited):
                if board[x1][y1] != ' ' and board[x1][y1] != word[p]: return
                
                if dfs(x1, y1, p+1, d): return True
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#': continue
                if board[i][j] == ' ' or board[i][j] == word[0]:
                    for k in direct:
                        # print(i, j, k, visited)
                        if (i, j, k) not in visited and dfs(i, j, 1, k):
                            return True
        

        # print(dfs(1, 2, 1, (0, -1)))
        return False


print(Solution().placeWordInCrossword(
[["#"," ","#"],[" "," ","a"],["#","#"," "]],
"abc"
))