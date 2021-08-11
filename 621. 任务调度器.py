class Solution:
    # 贪心 + 队列
    def leastInterval(self, tasks, n: int) -> int:
        import heapq

        heap = [0]*26
        for i in tasks: heap[ord(i) - ord('A')] -= 1
        heapq.heapify(heap)
        ans = 0
        while heap:
            item = heapq.heappop(heap)
            if item == 0: break
            ans += 1
            res = []
            if item < -1:
                res.append(item + 1)
            sign = 0
            i = 0
            while i < n and heap:
                one = heapq.heappop(heap)
                if not one:
                    sign = 1
                    break
                if one < -1:
                    res.append(1 + one)
                
                i += 1

            if res or (i == n-1 and not sign):  # 完整的一个轮回
                ans += n
                for i in res: 
                    heapq.heappush(heap, i)
            else: # 提早结束部分
                ans += i
        return ans
print(Solution().leastInterval(
["A","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
,29
))