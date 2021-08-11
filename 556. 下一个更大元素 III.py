class Solution:
    def nextGreaterElement(self, n: int) -> int:
        from functools import reduce
        res = []
        while n:
            cur = n % 10
            res.append(cur)
            n //= 10
        ans = -1
        for i in range(1, len(res)):
            if res[i] < res[i-1]:
                for j in range(i):
                    if res[j] > res[i]: break
                res[i], res[j] = res[j], res[i]
                res[:i] = res[i-1::-1]
                ans = reduce(lambda x, y: x*10 + y, res[::-1])
                break
        print(ans)
        return ans if ans <= 0x7fffffff else -1

print(Solution().nextGreaterElement(2147483476))