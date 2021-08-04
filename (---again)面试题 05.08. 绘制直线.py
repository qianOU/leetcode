class Solution:
    # 默认二进制位都是1的屏幕显示
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int):
        cols = w // 32
        rows = length // cols
        ans = [0]*length
        head =  y*cols + x1 // 32
        tail =  y*cols + x2 // 32
        for i in range(head, tail+1):
            ans[i] = -1
        # 调整head 值， 高位补 0
        ans[head] = (ans[head] & 0xffffffff) >> x1 % 32 if x1 % 32 else -1
        # 调整末尾元素
        ans[tail] &= -0x80000000 >> x2 % 32 # 负数做右移，高位补 1

        return ans
    
print(Solution().drawLine(
15,
96,
81,
95,
1
))