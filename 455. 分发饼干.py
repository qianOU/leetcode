class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        a = sorted(g)
        b = sorted(s)
        count = 0
        p1 = p2 = 0
        n1, n2 = len(g), len(s)
        while p1 < n1 and p2 < n2:
            if a[p1] <= b[p2]:
                count += 1
                p1 += 1
                p2 += 1
            else：
                p2 += 1
        return count