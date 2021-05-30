class Solution:
    # 贪心  
    # step1 : 通过行变化将 1 调整到二进制的高位处， 
    # step2 : 列变化主要是为了调整出更多的 1
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if not grid[i][0]:
                grid[i] = [1-j for j in grid[i]]
        
        from collections import Counter
        # 每一列需要更多的1
        for i in range(n):
            a = Counter(grid[r][i] for i in range(m))
            if a[0] > a[1]:
                for row in range(m):
                    grid[row][i] = 1 - grid[row][i] 

        # 答案 汇总
        ans = 0
        for i in range(m):
            ans += sum(grid[i][j] << j for j in range(n))
        
        return ans