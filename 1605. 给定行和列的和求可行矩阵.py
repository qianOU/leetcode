class Solution:
    # 先填充行和以及列和最小的那个元素，就保证有解
    def restoreMatrix(self, rowSum, colSum): 
        m, n = len(rowSum), len(colSum)
        ans = [[0]*n for i in range(m)]

        from sortedcontainers import SortedList
        rows = SortedList()
        cols = SortedList()
        for i in range(m):
            rows.add((rowSum[i], i))

        for i in range(n):    
            cols.add((colSum[i], i))
        

        while rows and cols:

            (r_sum, r), (c_sum, c) = rows[0], cols[0]
            del rows[0]
            del cols[0]
            if r_sum > c_sum:
                ans[r][c] = c_sum
                rows.add((r_sum-c_sum, r))

            elif r_sum < c_sum:
                ans[r][c] = r_sum
                cols.add((c_sum-r_sum, c))
            else: ans[r][c] = r_sum
        
        

        return ans


print(Solution().restoreMatrix( [5,7,10], [8,6,8]))