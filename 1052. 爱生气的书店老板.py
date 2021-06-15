class Solution:
    def maxSatisfied(self, customers, grumpy, minutes: int) -> int:
        n = len(customers)
        # 构建两个前缀和 列表
        presum = [0] 
        sat = [0]
        for i in range(n):
            presum.append(presum[-1] + customers[i])
            sat.append(sat[-1] + customers[i]*(1-grumpy[i]))
        

        # 暴力寻找最值
        ans = 0
        for i in range(minutes, n+1):
            # sat[max(i-minutes, 0)] x 时间段左侧满意的数量
            # sat[-1] - sat[i] x 时间段右侧满意的数量
            # presum[i]-presum[i-minutes] x 时间段内 满意的数量
            ans = max(presum[i]-presum[i-minutes] + sat[max(i-minutes, 0)] + sat[-1] - sat[i], ans)
        return ans


print(Solution().maxSatisfied(
 [1,0,1,2,1,1,7,5], 
 [0,1,0,1,0,1,0,1],
  3
))