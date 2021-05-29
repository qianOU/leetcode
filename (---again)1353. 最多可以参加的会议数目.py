class Solution:
    # 暴力 超时
    def maxEvents(self, events) -> int:
        
        events.sort(key=lambda x:(x[0], x[1]-x[0])) # 按结束时间升序排列
        
        n = len(events)
        count = 0

        visited = [False] * (n+1)
        i = 0
        time = events[0][0]
        while i < n:
            if not visited[i] and events[i][0] <= time <= events[i][-1]:
                j = i
                while j < n:
                    if not visited[j] and events[j][0] <= time <= events[j][-1] and events[j][-1] < events[i][-1]:
                        visited[j] = True
                        count += 1
                        i = j
                        break
                    j += 1
                # # 如果截至日期都大于等于 i ， 将i 设为看过
                if j==n:
                    visited[i] = True
                    count += 1
                    i += 1

                while i<n and events[i][-1] <= time:
                    visited[i] = True
                    i+= 1   
                if i >= n:
                    break

                time = events[i][0] if time + 1 < events[i][0] else time + 1
        
        return count
            

    # 方法2： 贪心 + 优先队列
    # 每次将 在某一天能参加会议的全部入栈， 之后利用小根堆特性，只去参加 endtime 最小的会议
    def maxEvents(self, events):
        ans, T = 0, 0 # 记录参加的会议数目，最大天数
        from collections import defaultdict
        evt = defaultdict(list)

        for i, j in events:
            evt[i].append(j)
            T = max(T, j)
        
        import heapq
        ans = []
        count = 0
        for t in range(1, T+1):
            for j in evt[t]:heapq.heappush(ans, j)
            while ans and ans[0] < t: heapq.heappop(ans)
            if ans:
                count += 1
                heapq.heappop(ans)                
        
        return count
a = [[1, i] for i in range(1, 1000000)]

print(Solution().maxEvents(a))