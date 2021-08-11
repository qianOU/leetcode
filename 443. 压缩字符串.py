class Solution:
    # 三指针
    def compress(self, chars) -> int:
        n =  len(chars)
        if n == 1: return 1
        prev = 0 # 已经处理好的数组指针
        l = 0
        for r in range(n + 1):
            if r == n or (r < n and chars[l] != chars[r]):
                chars[prev] = chars[l]
                prev += 1
                if r == n - 1 and chars[l] != chars[r]:
                    chars[prev] = chars[r]
                    prev += 1
                # elif r == n - 1: r += 1
                if r - l > 1:
                    nxt = str(r - l)
                    chars[prev: prev+len(nxt)] = nxt
                    prev += len(nxt)
                l = r

        return prev  

print(Solution().compress(["a","b","c"]))