class Solution:
    # 二分查找
    def findBestValue(self, arr, target: int) -> int:
        arr.sort()
        n = len(arr)

        presum = [0]
        for i in range(n):
            presum.append(presum[-1] + arr[i])

        total = presum[-1]
        
        print(presum)
        import bisect

        def find(l, r):
            mid = l + (r - l)//2
            idx = bisect.bisect_right(arr, mid)
            total = presum[idx] + (n-idx) * mid
            return abs(total - target)

        res = float('inf')
        ans = 0
        l, r = min(arr), max(arr)

        while l <= r:
            total = find(l, r)
            mid = (l + r)//2
            
            if total == 0:
                return mid
            total1 = find(mid+1, r)
            total2 = find(l, mid-1)
            print(l,r,mid, total, total1, total2)
            if total >= total1 > total2:
                r = mid - 1
            elif total >= total2 > total1:
                l = mid + 1
            else:
                return mid



print(Solution().findBestValue(
[4,9,3],
10))