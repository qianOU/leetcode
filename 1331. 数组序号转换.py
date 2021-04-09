class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        tmp = set(arr)
        a = len(tmp) + 1
        b = sorted(tmp)
        map_ = dict(zip(b, range(1, a)))
        return [map_[i] for i in arr]

