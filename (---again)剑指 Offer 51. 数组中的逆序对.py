class Solution:
    # 思路1： 红黑树 保持有序 + 二分查找
    def reversePairs(self, nums) -> int:
        from sortedcontainers import SortedList
        store = SortedList()

        n = len(nums)
        ans = 0
        #每次递加 以 i 为 逆序对 较小元素的 个数
        for i in nums:
            idx = store.bisect_left(-i)
            ans += idx
            store.add(-i)
        
        return ans
    
    # 思路2: 逆序对 联想到 归并排序
    def reversePairs(self, nums) -> int:
        n = len(nums)
        tmp = [0] * n # 临时数组， 归并有序是在原数组进行

        def merge_sort(l, r): # 左闭右闭区间
            if l == r: return 0
            mid = (l + r) // 2
            
            left, right = merge_sort(l, mid), merge_sort(mid+1, r)
            # 归并步骤
            tmp[l:r+1] = nums[l:r+1] # 移入暂存数组中
            p1, p2 = l, mid + 1
            cur, res = l, 0
            
            while cur <= r:
                print(p1, mid, p2, r)
                if p1 <= mid and (p2 > r or tmp[p1] <= tmp[p2]):
                    nums[cur] = tmp[p1]
                    p1 += 1
                    # 只要移动了左半部分的指针，就要更新逆序对的数量
                    res += p2 - mid - 1

                elif p2 <= r and (p1 > mid or tmp[p2] < tmp[p1]):
                    nums[cur] = tmp[p2]
                    p2 += 1

                cur += 1

            return left + right + res

        return merge_sort(0, len(nums)-1)
print(Solution().reversePairs([7,5,6,4,1,23,43,324,2,34]))