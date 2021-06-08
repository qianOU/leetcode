class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 矩阵上右下左依次编号为 1，2，3，4
        n = len(matrix)
        r_1, r_2 = n-1, n-1
        l_1, l_2 = 0, 0
        while l_1 <= r_1 and l_2 <= r_2:
            # 使用 O（n）空间
            tmp = [matrix[i][l_2] for i in range(r_1, l_1-1, -1)]

            for i in range(r_1 - l_1+1):
                # 3-4
                matrix[l_1 + i][l_2] = matrix[r_1][l_2 + i]
            for i in range(r_1 - l_1+1):
                # 2-3
                matrix[r_1][l_2+i] = matrix[r_1 - i][r_2]
            for i in range(r_1 - l_1+1):
                # 1->2
                matrix[r_1 - i][r_2] = matrix[l_1][r_2 - i]
            for i in range(r_1 - l_1+1):
                # 4->1
                matrix[l_1][l_2 + i] = tmp[i]
            
            l_1, l_2, r_1, r_2 = l_1 + 1, l_2 + 1, r_1 - 1, r_2 - 1

    # 真正的原地旋转
    # 其实只要能保证 matrix[row][col] => matrix[col][n-1-row]
    # step1 : 水平翻转
    # step2： 主对角线翻转
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 水平翻转
        for row in range(n>>1):
            for j in range(n):
                matrix[row][j], matrix[n-1-row][j] = matrix[n-1-row][j], matrix[row][j]

        # 主对角线翻转
        # 以主对角线元素为交换中心交换
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]