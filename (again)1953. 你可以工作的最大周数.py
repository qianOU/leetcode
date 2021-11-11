import heapq

class Solution:
    # 贪心
    def numberOfWeeks(self, milestones) -> int:
        n = len(milestones)
        tot = sum(milestones)
        max_element = max(milestones)
        if tot >= 2*max_element: return tot
        else: return 1 + 2*(tot - max_element)

print(Solution().numberOfWeeks([18,2,2]))