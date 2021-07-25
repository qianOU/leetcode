class Solution:
    # 找规律，值得注意的是对于当前位次出现的数字的情况进行讨论
    def countDigitOne(self, n: int) -> int:
        high, cur, low = n // 10, n % 10, 0
        digit, res = 1, 0
        while high or cur: # 当还没有完全扫描完数字的时候
            if cur == 0: res += high * digit
            elif cur == 1: res += high * digit + low + 1
            else: res += (high + 1) * digit
            # 移动 位 更新状态
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        
        return res

    # 基于递归的方法
    def countDigitOne(self, n: int) -> int:
        from functools import lru_cache
        
        @lru_cache(None)
        # [1--n] 中有多少个1
        def dfs(n):
            if n <= 0: return 0
            
            string = str(n)
            m = len(string)
            first = int(string[0])
            cur = 10**(m - 1)
            last = n % cur

            if first == 1: 
                return dfs(cur - 1) + dfs(last) + last + 1
            else:
                return first * dfs(cur - 1) + dfs(last) + cur

        return dfs(n) 

print(Solution().countDigitOne(1234))