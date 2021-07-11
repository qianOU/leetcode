class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)

        # 构建 start 和 index 的映射
        map_ = {l: i for i, (l, _) in enumerate(intervals)}
        
        ans = [-1]*n
        starts = sorted(i[0] for i in intervals)

        # 二分查找
        # 对于每个区间的右边界，在 start 构成的有序区间内 查找 第一个满足 start > r 的 start
        for i in range(n):
            l, r = 0, n-1
            target = intervals[i][-1]
            
            while l <= r:
                mid = (l + r) // 2
                if starts[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            if l >= n: ans[i] = -1
            else: ans[i] = map_[starts[l]]

        return ans
