class Solution:
    # 递归存在子问题， 每次将较大
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        @lru_cache(None)
        def dfs(i, j): #表示的是编号为 i--j 的凸边形的最低得分
            if j - i <= 1: return 0
            ans = float('inf')
            for k in range(i+1, j): # 与 边 i-j 形成三角形的另外一个顶点,切分成两个凸边形
                ans = min(ans, dfs(i, k) + dfs(k, j) + values[i]*values[j]*values[k])
            return ans
        
        return dfs(0, len(values)-1)