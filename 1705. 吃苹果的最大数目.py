import heapq
class Solution:
    # 贪心 优先吃保质期短的苹果 （堆）
    def eatenApples(self, apples, days) -> int:
        n = len(apples)
        heap = []
        for i in range(n):
            heapq.heappush(heap, (i+days[i], i, apples[i]))

        print(heap)
        ans = cur = 0 # 记录当前的日期
        while heap:
            dead, start, res = heapq.heappop(heap)
            if cur < start: 
                ans += start - cur
                cur = start
            if dead <= cur: continue
            eat = min(dead - cur, res)
            ans += eat
            cur += eat
        return ans



print(Solution().eatenApples(
[1,2,3,5,2],
[3,2,1,4,2]
))