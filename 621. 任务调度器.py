class Solution:
    # 思维1:模拟 贪心 + 堆
    # 贪心思维是每次拿数量较多的不同元素优先进行组合, 使用堆来维护
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
    
    # 思维2：填桶思想 十分的妙
    # https://leetcode-cn.com/problems/task-scheduler/solution/tian-tong-si-lu-you-tu-kan-wan-jiu-dong-by-mei-jia/
    def leastInterval(self, tasks, n: int) -> int:
        counter = Counter(tasks)
        max_num = counter.most_common(1)[0][1]
        last = sum(v == max_num  for v in counter.values())
        return max((n+1)*(max_num-1) + last, len(tasks))