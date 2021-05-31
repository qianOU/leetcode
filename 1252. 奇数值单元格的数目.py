class Solution:
    def oddCells(self, m: int, n: int, indices) -> int:
        rows = [0]*m
        cols = [0]*n
        for i, j in indices:
            rows[i] = (rows[i]+1)%2
            cols[j] = (cols[j]+1)%2

        print(rows, cols)
        length_1 = sum(cols)
        length_0 = n - length_1
        return sum(length_0 if  i else length_1 for i in rows)

print(Solution().oddCells(
2, n = 2, indices = [[1,1],[0,0]]
))