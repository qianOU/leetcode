class Solution:
    # 单序列 二维 动态规划
    # dp数组的状态定义十分巧妙，并且 状态转移的时候考虑的就是最后一个被搓破的气球，也十分巧妙！
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        # 按要求插入两个虚拟气球
        nums.insert(0, 1)
        nums.append(1)
        
        # dp数组
        dp = [[0]*(n+2) for i in range(n+2)]
        # dp[i][j] 表示的是搓破 开区间[i,...j] 所有气球能获得的最大分数
        #base - case 
        # 对于 j <= i+1 的都为 0
        # dp 数组的遍历方式 是 自底向上， 自左向右
        for i in range(n-1, -1, -1):
            for j in range(i+2, n+2):
                # 反向思考，考虑的是最后一个被搓破的气球
                # 对于最后一个被搓破的气球，有如下可能
                for k in range(i+1, j):
                    dp[i][j] = max(
                    dp[i][j],
                    dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j]
                    )

        return dp[0][n+1]
