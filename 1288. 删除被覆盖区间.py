class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0], -x[1]))
        i = 0
        n = len(intervals)
        count = 0
        max_last = 0
        for i in range(n):
            if  max_last >= intervals[i][1]:
                count += 1
            max_last = max(max_last, intervals[i][1])
        
        return n - count