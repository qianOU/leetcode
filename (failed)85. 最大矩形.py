class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix:
            return 0
        # 前缀和
        records = {}
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                records[(i, j)] = records.get((i-1, j), 0) + records.get((i, j-1), 0) - records.get((i-1, j-1), 0) + int(matrix[i][j])

        print(records)
        max_area = 0

        for i in range(m):
            for j in range(n):
                # max_area = max(max_area, matrix[i][j])
                for i2 in range(i, m):
                    for j2 in range(j, n):
                        item = records[(i2, j2)] - records[(i, j2)] - records[(i2, j)] + records[(i, j)]
                        print(i,j,i2,j2)
                        if item == max((i2-i)*(j2-j), i2-i, j2-j):
                            max_area = max(max_area, item)

        return max_area


print(Solution().maximalRectangle([[0,1,1,1,0,1,1,0]]))