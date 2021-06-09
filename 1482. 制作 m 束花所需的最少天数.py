class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        n = len(bloomDay)
        if k*m > n: return -1
        
        # 左右边界
        l, r = min(bloomDay), max(bloomDay)
        while l <= r:
            mid = l + (r-l) // 2
            count = 0 # 直接考虑在符合的最后一天开始收获所有的花
            prev = -1 # 不符合的位置
            for i in range(n):
                if bloomDay[i] > mid:
                    count += (i-prev-1) // k
                    prev = i

            count += (n-prev-1) // k
            print(l ,r, mid, count)
            if count < m: l = mid + 1
            else: r = mid - 1
        
        return l


print(Solution().minDays([1,10,3,10,2], 3, 1))