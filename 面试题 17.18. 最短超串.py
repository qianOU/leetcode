class Solution:
    # 滑动窗口
    def shortestSeq(self, big, small):
        from collections import defaultdict
        record = set(small)
        window = defaultdict(int)
        m, n = len(small), len(big)
        l = r = 0
        count = 0
        res = []
        ans = float('inf')
        while r < n:
            while r < n and count < m:
                if big[r] in record:
                    if window[big[r]] == 0: count += 1
                    window[big[r]] += 1
                r += 1

            if count != m: break
            # 更新答案
            if r - l < ans:
                ans = r - l
                res = [l, r-1]

            # 收缩左边界
            while l < r:
                if big[l] in record:
                    if window[big[l]] == 1:
                        if count == m and r - l < ans:  # 更新答案
                                ans, res = r - l, [l, r-1]
                        elif count == m - 1: break # 窗口的左边界位置
                        count -= 1
                    window[big[l]] -= 1
                l += 1
            
        return res


print(Solution().shortestSeq(
[842, 336, 777, 112, 789, 801, 922, 874, 634, 121, 390, 614, 179, 565, 740, 672, 624, 130, 555, 714, 9, 950, 887, 375, 312, 862, 304, 121, 360, 579, 937, 148, 614, 885, 836, 842, 505, 187, 210, 536, 763, 880, 652, 64, 272, 675, 33, 341, 101, 673, 995, 485, 16, 434, 540, 284, 567, 821, 994, 174, 634, 597, 919, 547, 340, 2, 512, 433, 323, 895, 965, 225, 702, 387, 632, 898, 297, 351, 936, 431, 468, 694, 287, 671, 190, 496, 80, 110, 491, 365, 504, 681, 672, 825, 277, 138, 778, 851, 732, 176]
,[950, 885, 702, 101, 312, 652, 555, 936, 842, 33, 634, 851, 174, 210, 287, 672, 994, 614, 732, 919, 504, 778, 340, 694, 880, 110, 777, 836, 365, 375, 536, 547, 887, 272, 995, 121, 225, 112, 740, 567, 898, 390, 579, 505, 351, 937, 825, 323, 874, 138, 512, 671, 297, 179, 277, 304]
))