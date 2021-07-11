class Solution:
    # lowbit 
    # 先判断 是否是 2 的幂次，其次判断 最低位 是 在 偶数位值即可
    def isPowerOfFour(self, n: int) -> bool:
        # 难点是如何 确定 1 是在 偶数位置
        
        mask = 0b01010101010101010101010101010101 # 将 32 位整数的 所有偶数位置为1
        mask = 0x55555555 # 将 超长的 2 进制每 4位一组合，形成 16 进制数据，简介
        return n > 0 and n & (n - 1) == 0 and n & mask != 0

    # 多项式解法 4**x 一定是 对 3 整除 余 1的（充分条件）
    # 如果是 2*4**x 形式，则 对 3 整除 余 2
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (-n) == n and n % 3 == 1
