class Solution:
    # 有向图 排序邻接表 + 回溯 （不排序的回溯超时）
    def findItinerary(self, tickets):
        from collections import defaultdict
        adj = defaultdict(list)
        visited =defaultdict(int) # 可能同两个节点之间有多张机票
        n = len(tickets)

        for start, end in tickets:
            adj[start].append(end)
            visited[(start, end)] += 1
        
        # 从小到大排序， 第一个满足就是排序最小的序列，直接返回即可
        for k in adj:
            adj[k].sort()

        ans = []
        def back_trace(cur, n, path):
            if not n:
                ans.append(path.copy())
                return True
            for j in adj[cur]: 
                if  visited[(cur, j)]:
                    visited[(cur, j)] -= 1
                    n -= 1
                    path.append(j)
                    if back_trace(j, n, path):
                        return True
                    # 撤销选择
                    visited[(cur, j)] += 1
                    path.pop()
                    n += 1

        back_trace('JFK', n, ['JFK'])

        return min(ans)