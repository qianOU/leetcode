class Solution:
    # 方法1： 完全回溯 超时
    def minimumEffortPath(self, heights) -> int:
        m, n = len(heights), len(heights[0])
        d = [(0, 1),  (1, 0), (-1, 0), (1, 0)]
        check = lambda x, y: 0<=x<m and 0<=y<n
        
        ans = float('inf')
        def dfs(i, j, prev, v, path):
            nonlocal ans
            if i==m-1 and j== n-1:
                ans = min(ans, max(v, abs(heights[m-1][n-1]-prev)))
                return
            
            for l, r in d:
                x, y = i+l, j+r
                if check(x, y) and (x,y) not in path:
                    path.add((x, y))
                    prev = heights[x][y]
                    v1 = max(v, prev-heights[i][j])
                    dfs(x, y, prev, v1, path)
                    path.discard((x, y))
            
        dfs(0,0, 0, 0, set())

        return ans


    # 方法二： 并查集
    # 抽象成图论问题， 边的权值为 两个邻接节点差值的绝对值
    # 主要思路就是， 先对边的权值排序，如果 首尾第一次呈现连通状态，则此时得到的 是最小体力消耗
    def minimumEffortPath(self, heights) -> int:
        class Ufoid:
            def __init__(self, n):
                self.parents = list(range(n))
                self.count = n
            
            def find(self, a):
                while a != self.parents[a]:
                    self.parents[a] = self.parents[self.parents[a]]
                    a = self.parents[a]
                return a
            
            def union(self, a, b):
                root_a, root_b = self.find(a), self.find(b)
                if root_a == root_b:
                    return 
                if root_a < root_b:
                    self.parents[root_b] = root_a
                else:
                    self.parents[root_a] = root_b
                
                self.count -= 1
            
            def connect(self, a, b):
                return self.find(a) == self.find(b)
        
        m, n = len(heights), len(heights[0])
        if m == n == 1:
            return 0
        edges = []
        for i in range(m):
            for j in range(n):
                if i > 0:
                    edges.append(((i-1)*n+j, i*n+j, abs(heights[i][j] - heights[i-1][j])))
                if j > 0:
                    edges.append((i*n+j-1, i*n+j, abs(heights[i][j-1] - heights[i][j])))

        
        edges.sort(key=lambda x: x[-1])
        
        uf = Ufoid(m*n)
        prev = edges[0][-1]
        for i in edges:
            if uf.connect(0, m*n-1):
                return prev[-1]
            prev = i
            uf.union(i[0], i[1])

        return prev[-1]



print(Solution().minimumEffortPath(
[[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]))