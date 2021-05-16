class Solution:
    def merge(self, intervals) :    
        if not intervals:
            return []

        # 按区间右边界排序
        intervals.sort()
        area_start, area_end = intervals[0]
        
        ans = []
        for i, j in intervals[1:]:
            if i <= area_end: # 代表两个区间是连通的， 由于左边界以及有序，所以只要确定扩大右边界
                area_end = max(area_end, j)
            else:
                ans.append([area_start, area_end])
                area_start, area_end = i, j
        
        ans.append([area_start, area_end])

        return ans

