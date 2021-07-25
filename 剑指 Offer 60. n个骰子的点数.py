class Solution:
    # 思路1： 分治算法 + 排列组合
    def dicesProbability(self, n: int) :
        from functools import reduce
        from collections import defaultdict
        
        # 计算[l,l+1,...r]的组合公式
        def mul(l, r):
            return reduce(lambda x, y: x * y, range(l, r+1), 1)

        # 分治
        def dfs(n):
            # 只有一个骰子的时候
            if n == 1:
                return dict(zip(range(1, 7), (1,)*6))
            
            mid = n // 2
            left, right = dfs(mid), dfs(n - mid)
            
            rec = defaultdict(int)

            # 归并两个组的次数
            for i in left:
                for j in right:
                    # 排列组合公式
                    rec[i+j] += (left[i] * right[j])*(mul(n - mid + 1, n)  / mul(1,  mid))
            
            return rec
        
        res = dfs(n) # python3 默认字典有序
        total = sum(res.values())
        return [v / total for v in res.values()]


    # 思路2: 动态规划
    # 本题存在明显的独立子问题性质，因此 dp 是比较好的方案
    def dicesProbability(self, n: int):
        # 两个状态，当前和 以及 骰子数
        dp = [[0]*70 for i in range(n+1)]
        for i in range(1, 7):
            dp[1][i] = 1

        for i in range(2, 1+n):
            for j in range(i, 6*i+1):
                # 做选择
                for s in range(1, 7):
                    if j - s >= 0:
                        dp[i][j] += dp[i-1][j - s]
                    elif j < s:break

        total = sum(dp[-1])
        return [dp[-1][j]/total for j in range(n, 6*n+1)]
    

    # 思路3: 动态规划的空间优化
    # 本题存在明显的独立子问题性质，因此 dp 是比较好的方案
    def dicesProbability(self, n: int):
        # 两个状态，当前和 以及 骰子数
        dp = [0]*70 
        for i in range(1, 7):
            dp[i] = 1

        for i in range(2, n+1):
            for j in range(6*i, i-1, -1):
                dp[j] = 0 # 新的阶段，将原始值置为 0 
                # 做选择
                for s in range(1, 7):
                    if j - s >= i-1: # 表示的是 j - s 是上一轮的投骰子的结果
                        dp[j] += dp[j-s] # 更新 
                    else: break

        total = sum(dp[n:])
        return [dp[j]/total for j in range(n, 6*n+1)]

print(Solution().dicesProbability(4))