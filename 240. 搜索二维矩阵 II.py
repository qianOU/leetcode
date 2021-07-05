class Solution:
    # 行， 列都是有序的
    # 思路1 从 左下角开始遍历
    # O(n+m)
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = m-1, 0 # 左下角
        # 从左下角 一直 遍历到 边界
        while x>=0 and y < n:
            if target == matrix[x][y]: return True
            elif  matrix[x][y] > target:
                    x -= 1
            else: 
                    y += 1

        return False