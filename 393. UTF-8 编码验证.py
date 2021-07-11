class Solution:
    # python 位运算 + 数组指针
    def validUtf8(self, data) -> bool:
        length = len(data) # 确定是几个字节的字符
        l = 0 # 数组指针
        while l < length:
            
            item = data[l]
            # 确定合理的字节数， 记录在 n 位置
            n = 0
            for i in range(4):
                if item >> (7-i) & 1:
                    n += 1
                else:
                    n = max(n, 1) 
                    break

            # 如果只有一个字节
            if n == 1:
                if (item >> 7) & 1:
                    return False
                l += 1 
                continue
            else:
                # 查看第一个字节是否符合要求，即在前导 n + 1 位是 0
                if (item >> 7 - n) & 1:
                    return False

                # 判定一个合理的UTF8字符的 [2,..n] 位是否是 高位 为 10
                for _ in range(1, n):
                    l += 1
                    # 如果数组指针超过数组长度，或者 最高位 不是 10 则是 False
                    if l >= length or (data[l] >> 6) ^ 2:
                        return False

                l += 1

        return True
    
print(Solution().validUtf8([235,140,4]))