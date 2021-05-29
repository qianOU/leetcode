class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        items = [min(i) for i in rectangles]
        return items.count(max(items))