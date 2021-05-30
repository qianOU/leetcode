class Solution:
    # 思路1： 动态规划
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        flowerbed = [0, *flowerbed, 0]
        m = len(flowerbed)

        # dp[i][j] 表示的是 在 在第 i 块场地的时候，选择 j 状态下能 种的最多花， 0-表示不种花， 1表示种花
        # 为何是二维的dp数组，是因为要符合题意，则当前的选择是基于 前一个场地的选择而做的
        # 所以需要一个维度表示选择
        dp = [[0]*2 for i in range(m)]

        for i in range(1, m-1):
            # 如果 i 的周边有 花朵了，则在此处不能种花，能得到的最大花数，自然是前一个状态的最大值
            if 1 in (flowerbed[i-1], flowerbed[i], flowerbed[i+1]):
                dp[i][0] = max(dp[i-1][1], dp[i-1][0])
            else:
                # 在i处选择不种花， 其最大花树也就是在 i-1 处种花数量
                dp[i][0] = dp[i-1][1]
                # 在i处选择种花， 其最大花树也就是在 i-1 处不种花数量 + 1
                dp[i][1] = dp[i-1][0] + 1
        
        return max(dp[m-2][0], dp[m-2][1]) >= n
    
    # 思路2：贪心 + 一次遍历
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        m = len(flowerbed)
        count = 0
        for i in range(0, m):
            left, right = max(i-1, 0), min(m-1, i+1)
            if flowerbed[left] or  flowerbed[i] or flowerbed[right]:
                continue
            else:
                count += 1
                if count >= n: return True
                flowerbed[i] = 1
        
        return False

print(Solution().canPlaceFlowers([1,0,0,0,1], 2))