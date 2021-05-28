class Solution:
    def possibleBipartition(self, n: int, dislikes) -> bool:
        adj = [[] for i in range(n+1)]
        for i, j in dislikes:
            adj[i].append(j)
            adj[j].append(i)
        
        flag = [0] * (n+1)
        visited = set()

        def dfs(i):
            if i in visited:
                return True
            visited.add(i)
            for j in adj[i]:
                if flag[j] == flag[i]:
                    return False
                elif not flag[j]:
                    # 如果是互相排斥的，染不同的颜色
                    flag[j] = -flag[i]
                    if not dfs(j):
                        return False
            return True


        for i in range(1, n+1):
            if i not in visited:
                flag[i] = 1 # 考虑在不同群体的时候
                if not dfs(i):
                    return False
        return True

print(Solution().possibleBipartition(
5,
[[1,2],[3,4],[4,5],[3,5]]
))