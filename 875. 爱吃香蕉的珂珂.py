class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        l, r = min(piles), max(piles)
        while l <= r:
            mid = l + (r-l) // 2
            time = 0
            for i in piles:
                # 吃完 i 需要的时间
                time += i // mid + min(i % mid, 1)
                if time > h:
                    break
            if time > h: l = mid + 1
            else: r = mid - 1
        
        return l


print(Solution().minEatingSpeed([3, 6,7,11], 8))