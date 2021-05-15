class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        from collections import Counter
        counter = Counter(arr)

        n = len(counter)

        # counts = sorted(counter.values())
        counts = counter.most_common()[::-1]
        
        for i in counts:
            if i <= k:
                k -= i
                n -= 1
        
        return n