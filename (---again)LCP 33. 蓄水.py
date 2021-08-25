class Solution:
    # 先枚举总的蓄水次数,再求得水桶的容量
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        max_time = max(vat)
        if max_time == 0: return 0
        ans = float('inf')
        for i in range(1, max_time+1): # 枚举蓄水的次数
            tmp = 0
            for b, v in zip(bucket, vat):
                new_b = math.ceil(v / i) # 是向上取整的
                tmp += max(0, new_b - b) # 加水的次数
            ans = min(ans, tmp + i)
        return ans