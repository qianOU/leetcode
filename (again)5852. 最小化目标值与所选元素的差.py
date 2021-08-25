class Solution:
    # 思路 1 DFS 剪枝
    def minimizeTheDifference(self, mat, target: int) -> int:
        m, n = len(mat), len(mat[0])
        self.ans = float('inf')
        for i in mat: i.sort() # 每一行排序进行剪枝
            
        @lru_cache(None)
        def dfs(cur, cum):
            if cur == m:
                self.ans = min(self.ans, abs(cum - target))
                return  
            for i in range(n):
                res = cum + mat[cur][i]
                if  res >= target and res - target >= self.ans: return
                dfs(cur+1, res)

        
        dfs(0, 0)
        return self.ans
    
    # 思路 2 动态规划
    def minimizeTheDifference(self, mat, target: int) -> int:
        m, n = len(mat), len(mat[0])
        dp = [0]*801 # target 最大为800
        dp[-1] = float('inf') # 记录 大于等于 800 的最小值
        for i in range(n):
            dp[mat[0][i]] = 1
        
        for i in range(1, m):
            dp[-1] = dp[-1] + mat[i][0]
            for p in range(799, 0, -1): # 倒序更新
                if dp[p]: # 上一行的结果
                    for j in range(n):
                        if mat[i][j] + p >= 800: 
                            dp[-1] = min(dp[-1], mat[i][j] + p)
                        else: dp[mat[i][j] + p] = 1
                    dp[p] = 0 # 转移到下一层，当前累计和变为不可达

        ans = float('inf')
        for i in range(800):
            if dp[i]: 
                ans = min(ans, abs(i - target))
                if i > target: return ans
        return min(dp[-1] - target, ans)


print(Solution().minimizeTheDifference(
[[65],[45],[45],[69],[55],[60],[29],[25],[16],[5],[62],[16],[29],[19],[34],[2],[24],[32],[66],[62],[60],[46],[42],[37],[51],[4],[41],[4],[66],[20],[9],[4],[66],[6],[56],[10],[51],[44],[7],[8],[5],[44],[28],[7],[10],[7],[24],[62],[19],[14],[45],[68],[9],[14],[51],[28],[8],[57],[59],[6],[54],[8],[19],[16],[63],[45],[33],[15],[33],[67]]
,800
))