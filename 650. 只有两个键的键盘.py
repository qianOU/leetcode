class Solution:
    # 思路1： DFS
    def minSteps(self, n: int) -> int:
        self.ans = n
        def dfs(cur, step, copy_num=0): # 禁止重复复制两次
            if step > self.ans: return
            if cur == n: 
                self.ans = min(self.ans, step)
                return
            if copy_num < cur:
                dfs(cur, step + 1, cur) # 执行复制
            if copy_num and n % copy_num == 0: # 数学性质，copy_num 一定是 n 的因子
                dfs(cur + copy_num, step + 1, copy_num) # 执行粘贴
        
        dfs(1, 0, 0)
        return self.ans
    
    # 思路2： 质数分解 为所有分解的质数之和
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n //= d
            d += 1

        return ans

    # 思路3: DP
    def minSteps(self, n: int) -> int:
        dp = [0]*(1+n) # dp[i] 表示的是产生 i 个 A 所需要的最小复制粘贴次数
        for i in range(2, 1+n):
            dp[i] = i
            for j in range(2, i//2 + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[-1]