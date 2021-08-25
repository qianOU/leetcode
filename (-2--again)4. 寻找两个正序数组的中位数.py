class Solution:
    # O(m + n) 的复杂度: 双指针
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m, n = len(nums1), len(nums2)
        k = (m + n) // 2 #中位数的索引
        astart = bstart = 0 
        prev = cur = -1
        # 循环次数为 k + 1
        for count in range(k+1):
            prev = cur
            # 移动 nums1 数组指针的情况
            if astart < m and (bstart >= n or nums1[astart] <= nums2[bstart]):
                cur = nums1[astart]
                astart += 1

            else:
                cur = nums2[bstart]
                bstart += 1
                

        if (m+n) & 1:
            return cur
        else:
            return (prev + cur) / 2

    # O(log(m + n)) 的复杂度,使用二分 + 递归处理,每次 排除一半的元素
    # 思想上有点类似 快排 寻找 TOP-k 问题
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m, n = len(nums1), len(nums2)

        # k 代表的是找寻 nums1 核 nums2 中 第 k 小的数字
        def dfs(nums1, nums2, k):
            print(nums1, nums2, k)
            m, n = len(nums1), len(nums2)
            if m == 0: return nums2[k-1]
            elif n == 0: return nums1[k-1]
            elif k == 1: return min(nums1[0], nums2[0])
            
            mid = k // 2 - 1
            p1, p2 = min(m-1, mid), min(n-1, mid)
            if nums1[p1] >= nums2[p2]:
                return dfs(nums1, nums2[p2+1:], k - (p2 + 1))
            else:
                return dfs(nums1[p1+1:], nums2, k - (p1 + 1))
        
        if (m + n) & 1:
            return dfs(nums1, nums2, (m + n) // 2 + 1) 
        return (dfs(nums1, nums2, (m + n) // 2) + dfs(nums1, nums2, (m + n ) // 2 + 1)) / 2
    
    # O(log(min(m, n))) 的复杂度,使用二分 + 递归处理
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m, n = len(nums1), len(nums2)
        if m > n: # 确保 nums1 长度是 小于 nums2
            nums1, nums2 = nums2, nums1
            m, n = n, m
        
        l, r = 0, m # 二分查找 切割位置
        while l <= r:
            i = (l + r) // 2 # nums1 的切割位置
            j = (n + m + 1) // 2 - i # nums2 的切割位置
            # 接下来要保证 左部分 的最大值 一定是 小于等于 右部分最小值的
            if j!=0 and i != m and nums2[j-1] > nums1[i]: # 调大 i
                    l = i + 1
            elif j!=n and i != 0 and nums1[i-1] > nums2[j]: # 调小 j
                    r = i - 1
            else: # 因为中位数一定存在，所以两个数组切割点在边缘的时候也是意味着两个数组中达到了切割的平衡点
                maxleft = 0
                if i==0: maxleft = nums2[j-1]
                elif j==0: maxleft = nums1[i-1]
                else: maxleft = max(nums1[i-1], nums2[j-1])
                if (m + n) & 1: return maxleft

                minright = 0
                if i==m: minright = nums2[j]
                elif j == n: minright = nums1[i]
                else: minright = min(nums2[j], nums1[i])
                return (maxleft + minright) / 2 
                    



print(Solution().findMedianSortedArrays(
[1,3],
[2]
))