class Solution:
    # 二进制 八皇后问题
    def maxCompatibilitySum(self, students, mentors) -> int:
        m, size = len(students), len(students[0])
        
        matrix = [[0]*m for i in range(m)]
        for i in range(m):
            for j in range(m):
                matrix[i][j] = sum(p==q for p,q in zip(students[i], mentors[j]))
        
        visited =  [0]*m
        res = 0
        def dfs(i, j, ans):
            nonlocal res
            if i == m:
                res = max(res, ans)
                return 
            
            for j in range(m):
                if  not visited[j]:
                    visited[j] = 1
                    dfs(i + 1, j, ans + matrix[i][j])
                    visited[j] = 0

        for i in range(m):
            dfs(0, i, 0)
        
        return res


print(Solution().maxCompatibilitySum(
[[0,1,0,1,1,1],[1,0,0,1,0,1],[1,0,1,1,0,0]],
[[1,0,0,0,0,1],[0,1,0,0,1,1],[0,1,0,0,1,1]]
))