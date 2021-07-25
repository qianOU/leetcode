class Solution:
    # 约瑟夫环问题 ()
    def lastRemaining(self, n: int, m: int) -> int:
        res = 0
        for i in range(2, n+1): # 数组长度枚举
            res = (res + m) % n
        return res

print(Solution().lastRemaining(

70866,
116922
))