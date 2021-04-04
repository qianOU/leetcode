class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """

        # step 1 找有效点
        min_ = float('inf')
        ans = -1
        for j in range(len(points)):
            p = points[j]
            i = (abs(x-p[0]), abs(y-p[1]))
            # print(i,j)
            if 0 in i and sum(i) < min_:
                ans = j
                min_ = sum(i)
        return ans

A = Solution()
print(A.nearestValidPoint(3,4, [[1,2],[3,1],[2,4],[2,3],[4,4]]))