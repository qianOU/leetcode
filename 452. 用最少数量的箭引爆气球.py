class Solution:
    # 基于左边界 以及 区间长度 升序排列， 贪心规则
    def findMinArrowShots(self, points) -> int:
        if not points:
            return 0

        points.sort(key=lambda x:(x[0], x[1]-x[0]))
        
        print(points)
        n = len(points)
        i = count = 0
        arr = points[0][-1]
        while i < n:
            while i<n and points[i][0] <= arr:
                if points[i][-1] < arr: # 如果 是 上一个的子区间，则改动 箭头 射的位置，确保 子区间也能被射爆
                    arr = points[i][-1]
                i += 1

            count += 1
            # 防止索引出界
            if i == n:
                break

            arr = points[i][-1]
            i += 1
            
        
        return count

    # 方法2： 基于右边界排序， 贪心
    def findMinArrowShots(self, points) -> int:
        points.sort(key=lambda x: x[1])
        count = 1
        arr = points[0][-1] # 基于贪心每次都射右边界
        for i, j in points[1:]:
            if i > arr:
                count += 1
                arr = j
        
        return count

print(Solution().findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))