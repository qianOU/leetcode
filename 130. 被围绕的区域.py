class Solution:
    # 效率比较低的 DFS 
    # 扫描所有的 0. 不满足的话再 重新置为 X，有重复遍历的情况
    # 更优的应该是从 二维矩阵边界 的 O开始扫描，得到的连通的 O 都是不符合的，剩下所有的 O 都是被 X 覆盖的
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(board), len(board[-1])
        check = lambda x,y: 0<=x<m and 0<=y<n
        visited = set()

        def dfs(i, j):
            count = 0
            ans = []
            for l, r in d:
                x, y = i+l, j+r
                if check(x, y):
                    if 0<x<m-1 and 0<y<n-1 and board[x][y] == 'O' and (x, y) not in visited:
                        visited.add((x, y))
                        a = dfs(x, y)
                        if a:
                            ans.extend(a)
                            count += 1

                    elif board[x][y] == 'X' or (x, y) in visited:
                            count += 1
            
            if count == 4:

                board[i][j] = 'X'
                ans.append((i, j))
                return ans
            
            for i,j in ans:
                board[i][j] = 'O'

            return 


        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and (i, j) not in visited:
                    visited.add((i, j))
                    dfs(i, j)

        return board

# print(Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
print(Solution().solve([["O","X","O","O","O","X"],["O","O","X","X","X","O"],["X","X","X","X","X","O"],["O","O","O","O","X","X"],["X","X","O","O","X","O"],["O","O","X","X","X","X"]]))