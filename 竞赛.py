class FindSumPairs:
    # 维护计数表
    def __init__(self, nums1, nums2):
        from collections import Counter
        self.nums1 = Counter(nums1)
        self.counter = Counter(nums2)
        self.nums2 = nums2
        
    def add(self, index: int, val: int) -> None:
        self.counter[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.counter[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for i in self.nums1:
            ans += self.counter[tot - i] * self.nums1[i] 
        return ans


obj = FindSumPairs(*[[1,1,2,2,2,3],[1,4,5,2,5,4]])
obj.add(3, 2)
param_2 = obj.count(8)