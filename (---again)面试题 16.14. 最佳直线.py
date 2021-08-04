class Solution:
    def bestLine(self, points):
        n = len(points)
        max_len = 0
        res = []
        for idx in range(n-1): # 遍历的是过 idx 点的直线
            i, p = points[idx]
            record = {}
            for j in range(idx+1, n):
                x, y  = points[j]
                if x == i:
                    key = None
                else:
                    key = (y-p)/(x-i)
                record.setdefault(key, [idx])
                record[key].append(j)     
            for key in record:
                if len(record[key]) > max_len:
                    max_len = len(record[key])
                    res = record[key][:2]

        return res


print(Solution().bestLine(
[[-13260,8589],[1350,8721],[-37222,-19547],[-54293,-29302],[-10489,-13241],[-19382,574],[5561,1033],[-22508,-13241],[-1542,20695],[9277,2820],[-32081,16145],[-50902,23701],[-8636,19504],[-17042,-28765],[-27132,-24156],[-48323,-4607],[30279,29922]]
))