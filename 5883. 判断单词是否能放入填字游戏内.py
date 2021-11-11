class Solution:
    def placeWordInCrossword(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])
        length = len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#' or (board[i][j] != ' ' and board[i][j] != word[0]): continue
                

print(Solution().placeWordInCrossword(
[["#"," ","#"],[" "," ","a"],["#","#"," "]],
"abc"
))