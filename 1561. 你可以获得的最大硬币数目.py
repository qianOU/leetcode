class Solution:
    # 写的复杂了些，思路是一致，可以使用简单的写法
    def maxCoins(self, piles: List[int]) -> int:
        arr = sorted(piles, reverse=True)
        n = len(arr)
        l, r = 0, n-1
        ans = 0
        # 每次取两个最大，再取一个最小的给bob策略
        while l <= r:
            ans += arr[l+1]
            l += 2
            r -= 1
        return ans
    
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort() # 从小到大排序
        n = len(piles)
        return sum(piles[n//3::2])