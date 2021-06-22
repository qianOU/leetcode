class Solution:
    # 深层暴力 + 一维前缀和（超时）
    def maxSideLength(self, mat, threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        # 前缀和
        rows = [[0] for i in range(n)] # rows[i] 表示第 i 行的前缀和

        for i in range(m):
            for j in range(n):
                rows[i].append(rows[i][-1] + mat[i][j])
        
        # 暴力
        for k in range(min(m, n), 0,-1): # k 是正方形边长
            # i,j 控制的是边长为 k 的矩阵的左上角
            for i in range(m-k+1): # row
                for j in range(n-k+1):
                    right = j + k # 每一行最右侧边界【开区间】
                    total = 0
                    # 
                    for idx in range(k):
                        total += rows[i+idx][right] - rows[i+idx][j]
                        if total > threshold:
                            break
                    else:
                        return k
    
    # 思路二：二维前缀和  + 二分
    def maxSideLength(self, mat, threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        # 二维前缀和 dp[i][j] 表示 已 mat[i-1][j-1] 为矩阵右下角的矩阵和
        dp = [[0]*(1+n) for i in range(m+1)] 

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i-1][j-1]
        
        ans = 0
        # 暴力
        l, r = 1, min(m, n) # 边长的范围
        # 最大边长是符合情况的右边界
        while l <= r:
            mid = (l+r)//2
            flag = 0
            # 找寻 mid 为边长的正方形是否存在
            for i in range(1, m-mid+2):
                for j in range(1, n-mid+2):
                    if dp[i+mid-1][j+mid-1] - dp[i-1][j+mid-1] - dp[i+mid-1][j-1] + dp[i-1][j-1] <= threshold:
                        l = mid + 1
                        flag = 1
                        break
                if flag: break
            else: # 缩小搜索范围
                r = mid - 1

        ans = max(ans, r)
        
        return ans

    # 优先遍历 头节点的可能情况（i，j） 之后 确定 以（i，j）为左上角节点的最大边长
    def maxSideLength(self, mat, threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        # 二维前缀和 dp[i][j] 表示 已 mat[i-1][j-1] 为矩阵右下角的矩阵和
        dp = [[0]*(1+n) for i in range(m+1)] 

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i-1][j-1]
        
        ans = 0
        # 暴力
        l, r = 1, min(m, n) # 边长的范围

        for i in range(1, m+1):
            for j in range(1, n+1):
                # ans 记录的是上一个节点能获得的最大边长长度
                for mid in range(ans+1, r+1):
                    if i+mid-1<=m and j+mid-1<=n and dp[i+mid-1][j+mid-1] - dp[i-1][j+mid-1] - dp[i+mid-1][j-1] + dp[i-1][j-1] <= threshold:
                        ans += 1
                    else:
                        break
        
        return ans

print(Solution().maxSideLength(
[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
,4
))