class Solution:
    # 二分搜索 找满足条件的最右边解 具体参考零神解析，将值相等的看成一个类
    # 贪心 + 二分查找
    def maxProfit(self, inventory, orders: int) -> int:
        l, T, r = 0, -1, max(inventory)
                               
        # 二分搜索，找寻阈值 T
        # 为何找寻 T 的右边界， 是因为 total 是 随着 mid 变小，而递增的，所以我们要找到 T使得，total 和 order 尽量接近
        while l <= r:
            mid =  (l+r)//2
            # total 随着 mid 的变大，而变小
            total = sum(i-mid for i in inventory if i >= mid) # 大于 mid 的都变成 mid
            if total <= orders: # 寻找右边界
                # T = mid
                r = mid - 1 # 要使 total 变大，也就使mid 变小
            elif total > orders:
                l = mid + 1 

        
        T = l

        resid = orders - sum(i-T for i in inventory if i >= T) 
        
        print(T, resid)
        # 左开右闭区间求和, 必须用 整除，不然对于大数float 转换为 int 的时候，会出现精度损失，或者使用 decimal包装 flat 对象
        range_sum = lambda x, y: (y+x+1)*(y-x)//2

       
        ans = 0
        for i in inventory:
            if i >= T:
                if resid > 0:
                    ans += range_sum(T-1, i) # 多的部分，也就是最后变化为 T-1 的部分
                    resid -= 1
                else:
                    ans += range_sum(T, i) # 正好就是最后变化为 T 的部分

        return ans % (10**9 + 7)
        
# class Solution:
#     def maxProfit(self, inventory, orders: int) -> int:
#         mod = 10**9 + 7
        
#         # 二分查找 T 值
#         l, r, T = 0, max(inventory), -1
#         while l <= r:
#             mid = (l + r) // 2
#             total = sum(ai - mid for ai in inventory if ai >= mid)
#             if total <= orders:
#                 T = mid
#                 r = mid - 1
#             else:
#                 l = mid + 1

        
#         range_sum = lambda x, y: (x + y) * (y - x + 1) // 2
        
#         rest = orders - sum(ai - T for ai in inventory if ai >= T)
#         print(T, rest)
#         ans = 0
#         for ai in inventory:
#             if ai >= T:
#                 if rest > 0:
#                     ans += range_sum(T, ai)
#                     rest -= 1
#                 else:
#                     ans += range_sum(T + 1, ai)
                    
#         return ans % mod


print(Solution().maxProfit([19,61,74,44,66,7,3,90,74,21,49,56,12,2,56,10,82,94,70,94,55,13,4,80,75,70,91,8,40,19,59,1,83,28,38,8,35]
,1540))