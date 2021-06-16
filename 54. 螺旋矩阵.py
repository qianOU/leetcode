class Solution:
    def spiralOrder(self, matrix):
        ans = []
        m, n = len(matrix), len(matrix[0])

        # 左上角闭，右下角开
        l_up_r, l_up_c, r_down_r, r_down_c = 0, 0, m, n

        while l_up_r < r_down_r and l_up_c < r_down_c:
            # 1 向右
            for i in range(l_up_c, r_down_c):
                ans.append(matrix[l_up_r][i])

            # 2 向下
            for i in range(l_up_r+1, r_down_r):
                ans.append(matrix[i][r_down_c-1])
            
            # 3 回退 行（只有在有高度差的条件下）
            if r_down_r - l_up_r > 1:
                for i in range(r_down_c-2, l_up_c-1, -1):
                    ans.append(matrix[r_down_r-1][i])
            
            # 4 回退 列 (在有高度差并且和行差的条件下)
            if r_down_r - l_up_r > 1 and r_down_c - l_up_c > 1:
                for i in range(r_down_r-2, l_up_r, -1):
                    ans.append(matrix[i][l_up_c])
            
            # 更新边界
            l_up_r, l_up_c, r_down_r, r_down_c = l_up_r+1, l_up_c+1, r_down_r-1, r_down_c-1
        
        return ans


print(Solution().spiralOrder(
[[7],[9],[6]]))


