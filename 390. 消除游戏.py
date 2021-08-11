class Solution:
    # 模拟 超时
    def lastRemaining(self, n: int) -> int:
        res = list(range(1, n+1))
        s = 1
        while len(res) > 1:
            if s > 0: 
                res = res[1::2]
            else: res = res[-2::-2][::-1]
            s*=-1
        return res[0]

    # # 从后往前看的递归
    def lastRemaining(self, n: int) -> int:
        import math
        if n <= 2: return n
        pos, k = 0, int(math.log(n, 2))
        # pos = 0 if k % 2 == 0 and (n // (1<<k-1)) % 2 == 0 else 1
        while k :
            if k % 2 :
                pos = pos * 2 + 1
            else: # 这里需要特别处理一下
                item = n // (1 << k - 1)
                pos = item - 2 - (item // 2 - pos - 1)*2
            k -= 1
        return pos + 1
print(Solution().lastRemaining(6))