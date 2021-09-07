class Solution:
    # 动态规划
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        from collections import defaultdict
        if poured <= 1: return 0 if query_row or query_glass else poured
        dp = [{0: poured}]
        has_next = poured - 1
        layer = 1
        while layer <= 100 and has_next:
            cur = defaultdict(int)
            has_next = False
            for i, j in dp[-1].items():
                if j > 1:
                    item = (j - 1) / 2
                    cur[i-1] += item
                    cur[i+1] += item
                    if max(cur[i-1], cur[i+1]) > 1: has_next = True
            dp.append(cur)
            layer += 1

        for i in range(len(dp)):
            print(i, dp[i])
        return  min(dp[query_row][-query_row + 2*query_glass], 1) if query_row < layer  else 0

print(Solution().champagneTower(
6,
2,
0
))