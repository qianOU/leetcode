class Solution:
    def addToArrayForm(self, num, k: int):
        import math
        if not k: return num
        ans = []
        for i in range(int(math.log10(k))+1, 0, -1):
            ans.append(k%(10**i)//(10**(i-1)))
        # 确保 ans 的长度 小于等于 num        
        if len(ans) > len(num):
            num, ans = ans, num

        m, n= len(ans), len(num)
        a, b = m-1, n-1
        more = 0
        print(ans, num)
        while  b >= 0:
            item = (num[b] + (ans[a] if a >= 0 else 0) + more)
            num[b] = item % 10
            more = int(item >= 10)
            print(a, b, more, num)
            # ans 长度小于 num师
            if a < 0 and not more:
                return num

            a -= 1
            b -= 1

        if more: num.insert(0, 1)    
        return num
        

print(Solution().addToArrayForm([9,9,9,9,9,9,9,9,9,9],
1))