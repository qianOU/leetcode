class Solution:
    # 副对角线遍历的左下角起点行坐标要不在 第一列 的 k 位置，要不就在 m-1 行位置， min(k, m-1)
    # 副对角线遍历的右上角起点行坐标要不在 第一行 的 k 位置，要不就在 n-1 行位置， max(0, k + 1 - n)
    # 由此我们就得到了 行索引 的变化 范围， [min(k, m - 1), max(0, k - n + 1) ] 利用 i + j = k 的性质，就知道了列索引的值
    def findDiagonalOrder(self, mat):
        m, n = len(mat), len(mat[0])
        res = []
        sign = 1
        for k in range(m + n - 1):
            if sign > 0:
                for i in range(min(k, m - 1), max(0, k - n + 1) - 1 , -1):
                    res.append(mat[i][ k - i])
            else:
                for i in range(max(0, k - n + 1), min(k, m - 1) - 1):
                    res.append(mat[i][k - i])
        return res


print(Solution().findDiagonalOrder([[2,3]]))