class Solution:
    # 从后往前遍历 较为复杂
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1 nums2 是非严格递减序列
        n1, n2 = len(nums1), len(nums2)
        i, j = n1-1, n2-1
        ans = 0
        # 双指针从后往前遍历
        while i >= 0 and j >= 0:
            # 如果 i < j and nums1[i] 小于 nums2[j], 基于贪心规则， i 再往前进位，找寻最大距离
            while 0<=i<=j and nums1[i] <= nums2[j]:
                    ans = max(ans, j - i)
                    i -= 1
            
            # 如果 满足 nums1[i] <= num2[j] 但是 i > j的情况，由于 nums1 的递减性质， i 进一步往前缩进
            if i>=0 and nums1[i] <= nums2[j]:
                i -= 1
            else: # 否则 nums1[i] > nums2[j]的时候，j需要缩进
                j -= 1

        return ans


    # 从前往后遍历
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1 nums2 是非严格递减序列
        n1, n2 = len(nums1), len(nums2)
        res = 0
        i = 0
        # 固定 nums2,找到第一个使得 nums1[i] <= nums2[j] 的 点
        for j in range(n2):
            while i < n1 and nums1[i] > nums2[j]: 
                i -= 1
            
            if i < n1: res = max(j-i, res)
        
        return res
