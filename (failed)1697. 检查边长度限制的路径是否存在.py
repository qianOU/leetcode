class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList, queries):
        dist = {}
        adj = [[] for i in range(n)]
        for i, j, v in edgeList:
            i, j = min(i, j), max(i, j)
            dist[(i, j)] = min(dist.get((i, j), float('inf')), v)
            adj[i].append(j)
            adj[j].append(i)
        
        from functools import lru_cache



print(Solution().distanceLimitedPathsExist(
13
,[[9,1,53],[3,2,66],[12,5,99],[9,7,26],[1,4,78],[11,1,62],[3,10,50],[12,1,71],[12,6,63],[1,10,63],[9,10,88],[9,11,59],[1,4,37],[4,2,63],[0,2,26],[6,12,98],[9,11,99],[4,5,40],[2,8,25],[4,2,35],[8,10,9],[11,9,25],[10,11,11],[7,6,89],[2,4,99],[10,4,63]]
,[[9,7,65],[9,6,1],[4,5,34],[10,8,43],[3,7,76],[4,2,15],[7,6,52],[2,0,50],[7,6,62],[1,0,81],[4,5,35],[0,11,86],[12,5,50],[11,2,2],[9,5,6],[12,0,95],[10,6,9],[9,4,73],[6,10,48],[12,0,91],[9,10,58],[9,8,73],[2,3,44],[7,11,83],[5,3,14],[6,2,33]]
))

