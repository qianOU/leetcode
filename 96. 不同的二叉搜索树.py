class Solution:
    @functools.lru_cache(1000)
    def numTrees(self, n: int) -> int:     
        if n == 0:
            return 1
        return sum(self.numTrees(m)*self.numTrees(n-m-1) for m in range(n))