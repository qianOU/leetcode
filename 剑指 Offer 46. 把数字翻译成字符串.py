class Solution:
    # 递归 从高位开始递归，写法不优美
    def translateNum(self, num: int) -> int:
        if not num: return 1
        import math
        n = int(math.log10(num)) # 位数， 从 0 开始计算

        # 从数字的高位开始递归
        def dfs(cur):
            if cur == n+1:
                return 1

            ans = 0
            # 每次选择截取 1 位数字，或者 2 位数字, 当二位数字的时候，不能有前导0
            for i, j in zip(range(2), [0, 10]):
                # 取出的元素
                item =  int(num // 10**(n - cur - i) % (10**(i+1)))
                if n - cur - i >= 0 and j <= item < 26:
                    ans += dfs(cur + i + 1)
            return ans

        return dfs(0)

    # 动态规划
    def translateNum(self, num: int) -> int:
        if not num: return 1

        # 转换成字符串，就不用大量数学运算了
        num = str(num)
        n = len(num) # 位数
        # dp[i] 表示的是 在 num 的 i 处
        dp = [0]*(n+1)
        # base case 
        dp[n] = dp[n-1] = 1
        for i in range(n-2, -1, -1):
            dp[i] += dp[i+1]
            if  num[i] != '0' and int(num[i:i+2]) < 26:
                dp[i] += dp[i+2]

        return dp[0]

    # 递归 : 从低位开始递归
    def translateNum(self, num: int) -> int:
        if num <= 9: return 1
        ba = num % 100
        # 二位不合理的时候，只能取一位数字进行对应的情况
        if ba <= 9 or ba >= 26: return self.translateNum(num // 10)
        # 去除 2 位的结果 + 去除 1 位的结果
        else: return self.translateNum(num // 100) + self.translateNum(num // 10) 
    
    
