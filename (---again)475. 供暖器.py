class Solution:
    # 方法1： 贪心 
    # 1. 对于每个房子选用离其最近的供暖点(大于等于房子位置或者小于等于房子的第一个供暖站)即可
    # 2. 对于整个系统而已，需要的是 覆盖每栋房子的最小半径的最大值，来实现系统覆盖
    def findRadius(self, houses, heaters) -> int:
        n = len(heaters)
        heaters.sort() # 排序
        prev = 0
        ans = 0
        for house in houses:
            # 二分找寻 第一个 大于等于 house 的加热器位置
            l, r =prev, n - 1
            while l <= r:
                mid = (l + r) // 2
                if heaters[mid] >= house:
                    r = mid - 1
                else: l = mid + 1
            
            # 得到大于房子位置的第一个 加热器的位置是 l
            more = min(l, n - 1)
            if heaters[more] == house: continue

            # 二分找寻 第一个 小于于等于 house 的加热器位置
            l, r =prev, n - 1
            while l <= r:
                mid = (l + r) // 2
                if heaters[mid] <= house:
                    l = mid + 1
                else: r = mid - 1
            
            less = max(r, 0)
            # 对于房屋 house 来说， 所需要的最短半径是 tmp
            tmp = min(abs(heaters[more] - house), abs(house - heaters[less]))
            # 对于整个系统而已，需要的是最长半径
            ans = max(ans, tmp)
        return ans

    # 基于半径的二分查找
    def findRadius(self, houses, heaters) -> int:
        m, n = len(houses), len(heaters)
        heaters.sort() # 排序
        houses.sort()

        # 查看半径为 r 的时候是否符合题意
        # 时间复杂度为 O(m)
        def helper(r):
            idx = 0
            for i in heaters:
                left, right = i - r, i + r
                while idx < m and left <= houses[idx] <= right:
                    idx += 1
                if idx == m: return True
            
            return False

        l, r = 0, 10**9
        while l <= r:
            mid = (l + r) >> 1
            if helper(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l







print(Solution().findRadius(
[1,1,1,1,1,1,999,999,999,999,999],
[499,500,501]
))