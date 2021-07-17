class Solution:
    # 解法 1： BFS
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 计算一个数 各个 位上数字之和
        def calculate(x):
            res = 0
            while x:
                res += x % 10
                x //= 10
            return res

        from collections import deque
        q = deque()
        q.append(0) # 将二维矩阵压缩成一维数组
        visited = set([0]) 
        d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        count = 0

        while q:
            item = q.popleft()
            r, c = divmod(item, n) # 将一维数组索引，重新转换为 二维 表示
            count += 1
            for i, j in d:
                x, y = r + i, c + j
                nxt = x*n + y
                if 0 <= x < m and 0 <= y < n and nxt not in visited \
                    and calculate(x) + calculate(y) <= k:
                    visited.add(nxt)
                    q.append(nxt)
        
        return count


    # 解法 2： 动态规划
    def movingCount(self, m: int, n: int, k: int) -> int:
        def calculate(x):
            res = 0
            while x:
                res += x % 10
                x //= 10
            return res
        
        count = 0
        dp = [0]*n

        ans = 0
        for i in range(m):
            dp[0] = calculate(i) <= k
            for j in range(n):
                if i == 0:
                    dp[j] = calculate(j) <= k
                
                if dp[j] or (j > 0 and dp[j-1]):
                    dp[j] = 1
                    ans += 1

        return ans
                
                

