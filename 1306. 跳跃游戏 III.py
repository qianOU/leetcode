class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        visited = set([start])
        n = len(arr)
        check = lambda x: 0<=x<n

        if not check(start):
            return False

        from functools import lru_cache
        @lru_cache(None)
        def dfs(i):
            if  not arr[i]:
                return True
            
            for j in [-1, 1]:
                if check(i+j*arr[i]) and i + j*arr[i] not in visited:
                    visited.add(i + j*arr[i])
                    if dfs(i + j*arr[i]):
                        return True
                    visited.discard(i + arr[i])

        return bool(dfs(start))