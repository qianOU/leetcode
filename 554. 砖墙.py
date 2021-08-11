class Solution:
    def leastBricks(self, wall) -> int:
        n = len(wall)
        from itertools import accumulate
        cum = [list(accumulate(item)) for item in wall]
        ans = defaultdict(int)
        for r in range(n):
            item = wall[r]
            res = 0
            for j in item[:-1]:
                res += j
                ans[res] += 1
        
        return n - max(ans)