class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        
        adj = [[] for i in range(n)]
        for i,j in edges:;
        adj[i].append(j)
        adj[j].append(i)

