class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        return sum([[i]*j for i, j in sorted(Counter(nums).items(), key = lambda x: (x[1], -x[0]))], [])