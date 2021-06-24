class Solution:
    def maxPoints(self, points) -> int:
        n = len(points)
        import collections
        records = collections.defaultdict(lambda :1)
        ans = 1
        for i in range(n-1):
            records.clear()
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 - x2 == 0:
                    k = None
                else:
                    k = (y1-y2)/(x1-x2)
                   
                records[k] += 1
                ans = max( records[k], ans)

        return ans + 1 if ans else 0


print(Solution().maxPoints(
# [[1,1],[2,2],[3,3]]
[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
))