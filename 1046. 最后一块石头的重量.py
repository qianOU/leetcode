class Solution:
    # 思路一： 有序列表
    def lastStoneWeight(self, stones: List[int]) -> int:
        from sortedcontainers import SortedList
        a = SortedList()
        for i in stones:
            a.add(i)
        
        while a:
            if len(a) == 1:
                return a.pop()
            x = a.pop()
            y = a.pop()
            if x != y:
                a.add(x-y)
    
    # 思路2： 小根堆
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap = [-i for i in stones]
        heapq.heapify(heap)

        while heap:
            if len(heap) == 1: return -1*heapq.heappop(heap)
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x != y: heapq.heappush(heap, x-y)
        
        return 0