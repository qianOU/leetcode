class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        a = sorted(boxTypes, key=lambda x:(-x[1], x[0]))
        ans = 0
        k = 0
        for i, j in a:
            if k + i < truckSize:
                ans += i*j
            else:
                ans += (truckSize - k)*j
                break
        return ans