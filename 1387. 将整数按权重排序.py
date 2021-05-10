class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def check(x):
            if x%2:
                x = x//2
            else:
                x = 3 * x + 1
            return 1 + check(x)
        
        arr = list(range(lo, hi+1))
        arr.sort(key=lambda x: (check(x), x))
        return arr[k-1]