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
        sorted_array = [0]*n
        
        # 后序遍历
        # 主要体现在后序合并的阶段
        def merge(l,  r, num1, num2):
            mid = (l + r) // 2
            res, lpt, rpt = 0, 0, 0
            cur = l
            
            while lpt < len(num1) and rpt < len(num2):
                if num1[lpt] <= num2[rpt]:
                    sorted_array[cur] = num1[lpt]
                    lpt += 1
                    res += rpt
                elif num1[lpt] > num2[rpt]:
                    sorted_array[cur] = num2[rpt]
                    rpt += 1
                
                cur += 1

            if rpt == len(num2):
                sorted_array[cur: r+1] = num1[lpt: ]
                res += rpt * (len(num1) - lpt)
            else:
                sorted_array[cur: r+1] = num2[rpt:]
            
            print(l, r, num1, num2, sorted_array[l:r+1])
            return res

        def sort(l, r):
            if l == r: 
                sorted_array[l] = nums[l]
                return 0
            mid = (l + r) // 2
            ans = sort(l, mid) + sort(mid+1, r)

            return ans + merge(l, r, nums[l:mid+1], nums[mid+1: r+1])
            
        
        item = sort(0, n-1)
        print(sorted_array)
        return item

print(Solution().reversePairs([7,5,6,4,1,23,43,324,2,34]))