class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        import collections
        map_ = collections.defaultdict(set)
        for i,j in edges:
            if i > j: i,j = j, i
            map_[i] = map_[i].add(j)