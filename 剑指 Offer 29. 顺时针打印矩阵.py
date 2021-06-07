class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        ans = []
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        visited = set()

        def dfs(i,j,  r,  b):
            
            l = j
            h = i
            # 首部元素
            ans.append(matrix[i][j])
            width = height = 0

            for n_j in range(j+1, r):
                width = 1
                ans.append(matrix[h][n_j])
            for n_i in range(i+1, b):
                height = 1
                ans.append(matrix[n_i][r-1])

            if height: # 只有存在高度差的时候才需要横向回走，不然是同一行
                for n_j in range(r-2, l-1, -1):
                    ans.append(matrix[b-1][n_j])

            if width: # 只有存在宽度差的时候，才需要往上走，不然是同一列
                for n_i in range(b-2, h, -1):
                    ans.append(matrix[n_i][l])

            if i+1<m and j+1<n and r-1>i+1 and b-1>j+1:
                dfs(i+1, j+1, r-1, b - 1)
        
        dfs(0,0, n, m)

        return ans