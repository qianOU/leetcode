class Solution:
    #二分搜索
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        decode = lambda x: divmod(x, n)
        l, r = 0, m*n - 1
        while l <= r:
            mid = l + (r-l) // 2
            i, j = decode(mid)
            if matrix[i][j] < target:
                l = mid + 1
            elif matrix[i][j] == target:
                return True
            else:
                r = mid - 1
            
        return False
