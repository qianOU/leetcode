class Solution:
    # 计数法, twosum 问题的变种
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        from collections import defaultdict
        records = defaultdict(int)
        ans = []
        for i in nums:
            if records.get(target-i):
                ans.append([i, target-i])
                records[target-i] -= 1
                continue
            
            records[i] += 1
        return ans