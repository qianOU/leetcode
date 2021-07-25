class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        record = defaultdict(int)
        for i, j, c in segments:
            record[i] += c
            record[j] -= c

        res = []
        prev = total = left = 0
        for x in sorted(record):
            total += record[x]
            if prev: # 只需要判断某一个子区间颜色之和是否为0，不需要判断是否区间颜色是否相等，因为相等的情况也是对应这不同的颜色组合，也是需要拆离
                res.append([left, x, prev])
            prev = total
            left = x
        return res

