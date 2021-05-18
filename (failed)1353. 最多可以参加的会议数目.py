class Solution:
    # 区间合并
    def maxEvents(self, events) -> int:
        
        events.sort(key=lambda x:x[-1]) # 按结束时间升序排列
        ans = []
        area_l, area_r = events[0]
        

        

print(Solution().maxEvents([[1,2],[2,3],[3,4]]))