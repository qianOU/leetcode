class Solution:
    def pondSizes(self, land):
        d = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        m, n = len(land), len(land[0])
        check = lambda x, y: 0<=x<m and 0<=y<n

        def dfs(i, j):
            land[i][j] = 1
            count = 1
            for l, r in d:
                x, y = i+l, j+r
                if check(x, y) and not land[x][y]:
                    count += dfs(x, y)
                     # 已经遍历过的 置为 陆地
            
            return count
        

        # return dfs(0, 0)
        ans = []
        for i in range(m):
            for j in range(n):
                if not land[i][j]:
                    ans.append(dfs(i, j))
        
        return sorted(ans)


print(Solution().pondSizes([
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]))