class Solution:
    # 
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def dfs(nums1, nums2, k): # 找寻 num1 和 num2 中第 k 小的数字
            m, n = len(nums1), len(nums2)
            if m == 0: return nums2[k]
            if n == 0: return nums1[k]

            mid = k // 2
            if nums1[mid] 