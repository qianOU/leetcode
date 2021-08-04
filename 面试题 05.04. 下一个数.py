class Solution:
    # 掩码 01， 10 进行或运算
    # 使用 掩码 11 进行或运算, 遇见第一个 01的是较大值处, 10的是较小值交换处,其后记录 1 的个数,如果是较大值 k 个 1在最低位, 较小值的话,k个1是紧接着交换位的,
    def findClosedNumbers(self, num: int):
        if num == 0x7fffffff: return [-1, -1]
        min_ = max_ = -1
        k = 0
        for i in range(31):
            if  min_ < 0 and num & 3 == 2:
                min_ = (num ^ 3) << i | ((1 << k) - 1) << i-k

            if i<30 and max_ < 0 and num & 3 == 1:
                max_ = (num ^ 3) << i | ((1 << k) - 1)

            k += 1 if num&1 else 0
            
            num >>= 1
            

        return [max_, min_]
    
    # 上述思路的巧妙实现
    def findClosedNumbers(self, num: int):
        def nextOne(x):
            lowbit = x & -x
            tozero = x + lowbit
            # (x & ~tozero) 可以得到与转换位为 1 连续的所有的1,
            return (x & ~tozero) // lowbit >> 1 | tozero
        
        min_ = ~nextOne(~num)
        max_ = nextOne(num)
        min_ = min_ if 0< min_ < 0x7fffffff else -1
        max_ = max_ if 0< max_ < 0x7fffffff else -1
        return [max_, min_]

print(Solution().findClosedNumbers(
67))