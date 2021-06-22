class Solution:
    # 二分查找 + 前缀和
    # 数组和 随着 sum 的变大 而变大，即是严格单调递增的
    # 可以使用二分查找来加速
    # ps: 一个优化的点：就是利用绝对值函数的下凸函数性质
    # 找寻左边的v_lower, 使得 total <= target 且与 target 最近
    # 同理右边的 v_upper, 使得 total >= target 且与 target 最近
    # 实际上 我们观察可以发现 v_upper = v_lower + 1 的
    # 所以只需要搜寻 v_lower 即可
    def findBestValue(self, arr, target: int) -> int:
        arr.sort()
        n = len(arr)
        
        # 前缀和
        presum = [0]
        for i in range(n):
            presum.append(presum[-1] + arr[i])

        total = presum[-1]
        
        print(presum)
        import bisect


        res = float('inf')
        ans = float('inf')
        l, r = 0, max(arr) # 搜素范围为【0， 最大值】

        # erfen
        while l <= r:
            mid = l + (r - l)//2
            idx = bisect.bisect_right(arr, mid)
            total = presum[idx] + (n-idx) * mid
            
            if abs(total - target) < res:
                res = abs(total-target)
                ans = mid
            elif abs(total - target) == res:
                ans = min(ans ,mid)

            # 右半边界的收缩
            if total >= target:
                #要使得 total 变小， 也就是收缩右边界
                r = mid - 1
            # 左半边界的收缩
            elif total < target: # 增加 total
                l = mid + 1
           
        
        return ans