class Solution:
    # 字典 嵌套 字典
    def displayTable(self, orders) :
        from collections import defaultdict
        books = defaultdict(lambda : defaultdict(int))
        for _, i, j in orders:
            books[i][j] += 1
        

        tables = []
        foods = set()
        for item in books:
            tables.append(int(item))
            foods |= books[item].keys()

        m, n = len(tables), len(foods)
        dp = [[0]*(1+n) for i in range(1 + m)]
        tables.sort()
        # base - case
        dp[0][0] = 'Table'
        dp[0][1:] = sorted(foods)

        for i in range(1, 1+m):
            dp[i][0] = str(tables[i-1])
        
        for i in range(1, 1+m):
            for j in range(1, 1+n):
                dp[i][j] = str(books[dp[i][0]][dp[0][j]])
        
        return dp
