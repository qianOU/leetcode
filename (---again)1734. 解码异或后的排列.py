class Solution:
    # 位运算，需要搁个选取元素
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        tmp = 0
        for i in range(n-2, -1, -2):
            tmp ^= encoded[i] # ans[n-1] ^ ans[n-2] ^ ans[n-3] ^ ans[n-4] ^....^ ans[2] ^ ans[1]
        total = 1 if n%4 == 1 else 0 # 1 ^2 ^....^ n 利用了 异或与 4 的倍数关系
        ans = [total ^ tmp]
        for i in encoded:
            ans.append(ans[-1] ^ i)
        return ans