class Solution:
    # 初始的DFS解法
    # 两艘战舰之间至少有一个水平或垂直的空位分隔  这就 说明 有点类似 小岛问题
    def countBattleships(self, board: List[List[str]]) -> int: 
        m, n = len(board), len(board[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            if board[i][j] == 'X':
                board[i][j] = '.' # 遍历过置为 空
                for l, r in d:
                    x, y = i + l, j + r
                    if 0<=x<m and 0<=y<n and board[x][y] == 'X':
                        dfs(x, y)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    dfs(i, j)
                    ans += 1  
        
        return ans

    # 思路2： 如果X是战舰 则 其 左方和上方都没有战舰存在(这个判断可以表明X不是属于其它战舰的一部分)
    def countBattleships(self, board: List[List[str]]) -> int: 
        m, n = len(board), len(board[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (
                    (i==0 or board[i-1][j] == '.') and 
                    (j==0 or board[i][j-1] == '.')):
                    ans += 1

        return ans