class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        import math
        visited = {}
        res = []

        def dfs(a, b, k):
            if not a: return -1
            if a in visited:
                return visited[a]

            visited[a] = len(res)
            a*=10 # 小数除法，后移动一位相当于乘以 10
            # 此处可以使用二分加速
            l, r = 0, k
            while l <= r:
                mid = (l + r) >> 1
                if a * 10**mid >= b:
                    r = mid - 1
                else:
                    l = mid + 1

            a *= 10**l
            res.extend('0'*l)
            
            ele, nxt = divmod(a, b)
            res.append(str(ele))
            return dfs(nxt, b, k)

        sign = 0
        if (numerator ^ denominator) < 0: sign = -1
        interger, r = divmod(abs(numerator), abs(denominator))
        k = int(math.log10(abs(denominator))) + 1
        ans = str(interger)
        if r:
            idx =dfs(r, abs(denominator), k)
            if  idx < 0:
                ans = ans + '.' + ''.join(res) 
            else:
                ans  = ans  + '.' +  ''.join(res[:idx]) + '(' + ''.join(res[idx:]) + ')'
            
        return ans if not sign or (numerator == 0) else '-' + ans


print(Solution().fractionToDecimal(
7, -12
))