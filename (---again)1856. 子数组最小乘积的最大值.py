class Solution:
    # 暴力 超时
    def maxSumMinProduct(self, nums) -> int:
        n = len(nums)
        presum = [0] * (n+1) # 前n项和
        for i in range(1, n+1):
            presum[i] = presum[i-1]  + nums[i-1]
        
        max_ = 0
        for i in range(n-1):
            min_ = nums[i]
            for j in range(i, n):
                min_ = min(min_, nums[j])
                max_ = max(min_*(presum[j+1]-presum[i]), max_)

        return max_

    # 思路 就是用两个单调栈找到 某一个 元素 i ，左边界（小于 nums[i] 的左侧第一个元素索引）， 右边界（小于nuns[i]的右侧第一个元素索引）
    def maxSumMinProduct(self, nums) -> int:
        nums =nums 
        n = len(nums)
        mod = 10**9 + 7
        # presum = [0] * (n+1) # 前n项和
        presum = [0]*(1+n)
        for i in range(1, n+1):
            presum[i] = presum[i-1]  + nums[i-1]
            # presum.append(presum[-1] + nums[i])
        
        more_less = [[0,None,None] for i in range(n)]
        
        stack = []
        for i in range(n):
            more_less[i][0] = nums[i]
            # 栈顶元素如果大于 nums[i] 也就意味着找到右边界
            while stack and nums[stack[-1]] > nums[i]:
                item = stack.pop()
                more_less[item][-1] = i
            stack.append(i)
        # 还保留在栈中的元素，就是无右边界，设置为n
        while stack:
            item = stack.pop()
            more_less[item][-1] = n
        
        stack = []
        for i in range(n-1, -1, -1):
            # 栈顶元素如果大于 nums[i] 也就意味着找到左边界
            while stack and nums[stack[-1]] > nums[i]:
                item = stack.pop()
                more_less[item][1] = i+1 # 因为浅醉和每一个元素都是左闭右开的，所以左边界要+1

            stack.append(i)
        # 还保留在栈中的元素，就是无左边界，设置为0, presum[0] == 0
        while stack:
            item = stack.pop()
            more_less[item][1] = 0
        
        # 求余一定要在max 之后
        return max(map(lambda x:x[0]*(presum[x[-1]]-presum[x[1]]), more_less)) %mod