class Solution:
    # 回溯问题 
    # 优化：可以使用二进制来节约空间，以及 在 O(1) 的时间复杂度下进行判断是否可行
    def totalNQueens(self, n: int) -> int:
        def check(x, y, path):
            
            for i in range(n):
                # 查看 x 行
                if i!= y and x*n + i in path: return False
                # 查看 y 列
                if i!= x and n*i + y in path: return False
            
            # 主对角线
            k = x - y
            for i in range(max(k, 0), min(n - 1, k + n - 1) + 1):
                if i != x and i*n + (i - k) in path: return False
            
            # 副对角线
            k = x + y
            for i in range(max(0, k - n + 1), min(k, n-1) + 1 ):
                if i != x and i*n + (k - i) in path: return False
            
            return True
    

        def dfs(cur, path):
            if cur == n:
                return 1
            
            ans = 0
            for i in range(n):
                if check(cur, i, path):
                    path.append(cur*n + i)

                    ans += dfs(cur+1, path)

                    path.pop()
            return ans 

        return dfs(0, [])

    # 优化： 空间优化 使用 二进制
    def totalNQueens(self, n: int) -> int:
    
        # 在 cur行 做决策
        # columns 是 行状态， diag1 是主对角线， diag2 是副对角线 的 N 位二进制表示
        # 二进制位次是有以下规律： 棋盘的左边界是最低位，最右侧是最高位
        def dfs(cur, columns, diag1, diag2):
            if cur == n: return 1
            
            ans = 0
            # 查看可以在 cur 行 放 皇后的位置
            avaliable = ((1<<n) - 1) & (~(columns | diag1 | diag2))
            while avaliable:
                # 在最低位为 1的 位置
                position = avaliable & (-avaliable)
                avaliable &= avaliable - 1 # 将最低位的 1 置为 0  
                ans += dfs(cur+1, columns | position, (diag1 | position) << 1, (diag2 | position) >> 1)

            return ans
            
        return dfs(0, 0, 0, 0)

print(Solution().totalNQueens(8))