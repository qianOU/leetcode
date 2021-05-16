class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        for i in range(n):
            if newInterval[0] < intervals[i][0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                break
            res.append(intervals[i])
        
        ans = []
        area_l, area_r = res[0]
        for i, j in res:
            if i <= area_r:
                area_r = max(area_r, j)
            else:
                ans.append([area_l, area_r])
                area_l, area_r = i, j
        
        return ans