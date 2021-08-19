class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        x, y, z = jug1Capacity, jug2Capacity, targetCapacity
        if z == 0: return True
        if z >= x + y: return z == x + y 
        memory = {}

        def dfs(cap1, cap2):
            if cap1 + cap2 == z: return True
            if (cap1, cap2) in memory: return False # 回到以遍历的位置，就是不可能实现的情况
            memory[(cap1, cap2)] = False
            nxt = [(max(0, cap1 - (y - cap2)), min(y, cap2 + cap1)), (x, cap2),  (0, cap2), 
                    (min(x, cap1 + cap2), max(0, cap2 - (x - cap1))), (cap1, y), (cap1, 0)]
            for i, j in nxt:
                if  (i, j) not in memory and dfs(i, j):
                    return True
            
            return False

        return dfs(0, 0)

print(Solution().canMeasureWater(
13,
11,
1
))