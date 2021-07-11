class Solution:
    # 方法1： 贪心思维， 若冲突删除时间跨度大的区间部分
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 先按区间右侧排序，其次是按 区间 长短 从 小到 大 排序
        intervals.sort(key=lambda x: (x[-1], -x[0]))
        ans = 0

        n = len(intervals)
        end = intervals[0][1]

        for i in range(1, n):
            # 如果 i 和 之前的区间冲突了，则删除有较长区间范围的 i 区间
            if intervals[i][0] < end:
                ans += 1
            else:
                end = intervals[i][1]
        
        return ans

    
     # 方法2： (failed) 具有 LIS 性质的 DP 问题 优化方案 时间复杂度 为 0(NlgN)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        tails = [] # tails 表示的是 在 不重复区间长度为 i 的时候，最短的区间范围 即 区间右边界最小
        ans = 0 # 记录最长不重复区间的长度
        
        # 确保区间的左边界是递增的
        intervals.sort()
        
        # tails 是递增的
        for i, j in intervals:
            if tails and i < tails[ans-1]: continue
            if not tails or i >= tails[ans-1]:
                tails.append(j)
                ans += 1
            
            else:
                loc = None
                l, r = 0, ans - 1
                while l <= r:
                    mid = (l + r) // 2
                    if i < tails[mid]:
                        r = mid - 1
                        continue
                    if tails[mid] >= j:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                
                if loc is not None: tails[loc] = j
        
        return len(intervals) - ans

