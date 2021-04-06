class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for k in range(n):
            stand = matrix[0][k]
            for i in range(1, m):
                j = i+k
                if  j>=n:
                    break
                if matrix[i][j] != stand:
                    return False

        for k in range(1, m):
            stand = matrix[k][0]
            for j in range(1, n):
                i = j + k
                if i >= m:
                    break
                if matrix[i][j] != stand:
                    return False
                
        return True