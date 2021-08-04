class Solution:
    # hash 表 :  在确保子区间和大于1的前提下，找寻最大区间长度
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        presum = [0]
        for i in hours:
            i = 1 if i > 8 else -1
            presum.append(presum[-1] + i)

        record = {}
        ans = 0
        for i in range(len(presum)):
            # 注意这里需要取最小值，是因为对于 presum[i] - 1 大于 0 的时候，基于贪心的规则我们要选取 0 作为子区间起始点
            if min(presum[i] - 1, 0) in record:
                ans = max(ans, i - record[min(presum[i] - 1, 0)])
            if presum[i] not in record: # 只更新最左侧的索引
                record[presum[i]] = i
        return ans
    
    # 单调栈
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        presum = [0]
        for i in hours:
            i = 1 if i > 8 else -1
            presum.append(presum[-1] + i)

        # 首先构建一个单调递减栈，作为子区间的左端点
        stack = []
        for i in range(len(presum)):
            if not stack or presum[stack[-1]] > presum[i]:
                stack.append(i)
        
        # 从后往前遍历 presum 找寻最大的子区间右端点
        ans = 0
        for j in range(len(presum)-1, -1, -1):
            if not stack: break
            while stack and presum[stack[-1]] < presum[j]:
                ans = max(ans, j - stack[-1])
                stack.pop()
             
        
        return ans