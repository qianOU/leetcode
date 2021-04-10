class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mid = int(area**.5)
        for w in range(mid, 0, -1):
            l = area / w
            if int(l) == l:
                return [int(l), w]
