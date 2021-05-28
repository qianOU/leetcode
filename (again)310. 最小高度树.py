class Solution:
    # 思路一 ： dfs + 记忆化
    def findMinHeightTrees(self, n: int, edges):
        if not edges:
            return [0]
        
        adj = [[] for i in range(n)]
        visited = set()
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
          

        memo = {} # 记忆化
        def dfs(a, b): # a->b 路径子树的最大深度是多少（包括已知的a->b路径）
            if memo.get((a, b)):
                return memo.get((a, b))

            memo[(a, b)] = 1 # 包括已知的a->b路径
            for i in adj[b]:
                if i != a: # 因为不含有环，所以直接判断后继节点与前继节点不同就可以保证不走回头路
                    memo[(a, b)] = max(memo[(a, b)], dfs(b, i)+1)

            return memo[(a, b)]
        

        def helper(root): # 找寻 root 为 根节点的子树 最大深度
            count = 0
            for i in adj[root]:
                count = max(count, dfs(root, i)) # 也就是求 root -> i路径的最大深度
            return count 


        ans = []
        count = 2*10**4
        for i in range(n):
            item = helper(i)
            if item < count:
                ans.clear()
                ans.append(i)
                count = item
            elif item == count:
                ans.append(i)

        return ans
    
    # 思路二： 更优的方法  拓扑排序 + 多源 BFS 找寻平衡点（中点）
    # 从出度为 1 的叶子节点开始不断 BFS (由于是无向图，所以出度为 1 的才是 叶子节点)
    def findMinHeightTrees(self, n: int, edges):
        if not edges:
            return [0]
        
        adj = [[] for i in range(n)]
        outdegree = [0] * n
        visited = set()
        for i,j in edges:
            adj[i].append(j)
            outdegree[i] += 1
            adj[j].append(i)
            outdegree[j] += 1
        
        from collections import deque
        q = deque()
        # 出度为 1 的入队列
        for i in range(n):
            if outdegree[i] == 1:
                q.append(i)
        
        # 从叶子节点出发进行BFS，就相当于找中点
        while q:
            sz = len(q)
            res = [] # 每一层的叶子节点用数组来记录
            for _ in range(sz):
                cur = q.popleft()
                res.append(cur)
                for j in adj[cur]:
                    outdegree[j] -= 1
                    if outdegree[j] == 1: # 如果 j 变为 叶子节点，则入队列
                        q.append(j)
        
        return res
                