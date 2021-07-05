class Solution:
    # 回溯，每个棋子只有 横着 或者 竖着 两种姿态(向右，向下)
    def domino(self, n: int, m: int, broken) -> int:
        ans = 0
        mat = [[1]*m for i in range(n)]
        for i, j in broken:
            mat[i][j] = 0

        print(mat)
        def dfs(i, j, num):
            nonlocal ans
            print(i, j, num)
            if i == n:
                ans = max(ans, num)
                return

            if not mat[i][j]:
                c = j
                while c < m and not mat[i][c]:
                    c += 1
                if c < m:
                    dfs(i, c, num) 
                else:
                    dfs(i+1, 0, num) 
                return


            mat[i][j] = 0
            # 向右
            if i<n and j + 1 < m and  mat[i][j+1]:
                # 选择
                mat[i][j+1] = 0
                dfs(i, j+1, num+1)
                mat[i][j+1] = 1
            elif j+1 == m:
                dfs(i+1, 0, num)
            
            # 向下 
            if i + 1 < n and j < m and mat[i+1][j]:
                # 选择
                mat[i+1][j] = 0
                dfs(i+1, j, num+1)
                mat[i+1][j] = 1

            mat[i][j] = 1
        
        dfs(0, 0, 0)
        return ans

print(Solution().domino(
3,
3,
[]
))