class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []

        def dfs(i, n, path):
            if i == n-1:
                ans.append(path.copy())
                return
            
            for j in path[i]:
                dfs(j, n, path + [j])
        
        dfs(0, len(graph), [])

        return ans