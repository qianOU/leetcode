# 使用 两个堆，并且确保 小根堆 数量 始终大于等于 大根堆的数量
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        import heapq
        self.small = []
        self.big = []
        heapq.heapify(self.small)
        heapq.heapify(self.big)
        self.len1 = self.len2 = 0
       


    def addNum(self, num: int) -> None:
        heapq.heappush(self.big, num)
        one = heapq.heappop(self.big)
        heapq.heappush(self.small, -one)
        # 如果小根堆的数量大于大根堆 + 1，则将 小根堆中的 最小元素 加入 大根堆中
        if self.len1 > self.len2:
            one = heapq.heappop(self.small)
            heapq.heappush(self.big, -one)
            self.len2 += 1
        else:
            self.len1 += 1

    def findMedian(self) -> float:
        if (self.len1 ^ self.len2) & 1: # 奇数情况，记得加括号
            return -self.small[0]
        else:
            return (-self.small[0] + self.big[0]) / 2