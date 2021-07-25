
# class Solution:
#     def smallestChair(self, times, targetFriend: int) -> int:
#         tmp = sorted([i, j] for j, i in enumerate(times))
#         print(tmp)
#         from sortedcontainers import SortedList
#         outs = SortedList()
#         n = len(times)
#         prev = 0
#         import heapq
#         q = list(range(n))
#         records = {}
#         for [into, out], idx in tmp:
#             l, r = prev, len(outs) - 1
#             while l <= r: 
#                 mid = (l + r) // 2
#                 if outs[mid][0] <= into:
#                     l = mid + 1
#                 else: r = mid - 1
            
#             if   r >= prev:
#                 for _, j in outs[prev: r+1]:
#                     heapq.heappush(q, records[j])
#                     del records[j]
                
#                 prev = r + 1
                
#             records[idx] = heapq.heappop(q)
#             print(records)
#             if idx == targetFriend: return records[idx]
#             outs.add((out, idx))


# class Solution:
#     # 单调队列
#     def canSeePersonsCount(self, heights) :
#         n = len(heights)
#         heights.append(float('inf'))
#         stack = []
#         res = [0]*n
#         for i in range(n-1, -1, -1):
#             while stack and heights[stack[-1]] <= heights[i]:
#                 stack.pop()
#             res[i] = 0 if not stack else 
#             stack.append(i)
#         return res

class Solution:
    def splitPainting(self, segments):
        segments.sort(key = lambda x: x)
        res = []
        cur = segments[0][-1]
        left, cur = segments[0][:2]
        color = set([segments[0][-1]])
        for idx, (l, r, c) in enumerate(segments[1:]):
            color.add(c)
            if l <= cur:
                res.append([left, l, sum(color)  + (0 if l == cur else c)])
                left, color = cur, set([segments[1 + idx][-1]] if l == cur else color)
            else: 
                cur = max(cur, r) 

        res.append([left, cur, sum(color)])

        return res

print(Solution().splitPainting([[1,7,9],[6,8,15],[8,10,7]]))

# print(Solution().canSeePersonsCount(
# [10,6,8,5,11,9]
# ))

# print(Solution().smallestChair(
# [[33889,98676],[80071,89737],[44118,52565],[52992,84310],[78492,88209],[21695,67063],[84622,95452],[98048,98856],[98411,99433],[55333,56548],[65375,88566],[55011,62821],[48548,48656],[87396,94825],[55273,81868],[75629,91467]]
# ,6
# ))