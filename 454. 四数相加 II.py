class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        from collections import defaultdict
        
        def get(nums1, nums2):
            n = len(nums1)
            one = defaultdict(int)
            for i in range(n):
                for j in range(i, n):
                    one[nums1[i] + nums2[j]] += 1
            
            return one
        
        one = get(nums1, nums2)
        two = get(nums3, nums4)

        ans = 0
        for i in one:
            ans += two[-i]
        
        return ans
