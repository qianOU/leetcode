class Solution:
    # 基于 优先队列
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        from queue import PriorityQueue as pq
        q = pq()

        for i in range(n):
            q.put((matrix[i][0], i, 0))

        count = 0

        while count < k:
            item, row, idx = q.get()
            count += 1
            if idx >= n-1:
                continue
            q.put((matrix[row][idx+1], row, idx))
        
        return item

    # 基于 值 的二分查找
    # 本题特性 知道矩阵的 最小值和最大值
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            num = 0 # 小于等于 mid 的数量

            l, r = 0, n - 1
            # 从左下角开始遍历
            while l < n and r >= 0:
                if matrix[r][l] <= mid:
                    l += 1
                    num += r + 1
                else:
                    r -= 1
            
            return num 
        
        # 二分查找收缩符合条件的左边界，因为 符合 item == k 的 mid 可能是不存在于 矩阵中，
        # 但是 因为 矩阵保证了这样的数的存在，且一定是 二分搜索的左边界 因为 mid 等于矩阵第k个数的值时， 是二分搜索的左边界
        left = matrix[0][0]
        right = matrix[n-1][n-1]
        while left <= right:
            mid = (left + right) // 2
            item = check(mid)
            if item >= k: 
                right = mid - 1
            else:
                left = mid + 1
        
        return left