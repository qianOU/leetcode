class Solution:
    def intersect(self, nums1 , nums2 ):
        from collections import Counter
        a = Counter(nums1)
        b = Counter(nums2)
        comm = a.keys() & b.keys()
        print(a, b, comm)
        res = []
        for i in comm:
             res.extend([i]*min(a[i], b[i]))
        return res

print(Solution().intersect([1,2,2,1],[2,2]))