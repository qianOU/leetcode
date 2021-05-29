class Solution:
    #思路1  基数排序 0(k*N)
    def maximumGap(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return 0

        import math
        # 注意在关于 10 取对数之后，需要 + 1
        k = math.ceil(math.log10(max(nums))) + 1 # 最大数一共有 k 位

        for i in range(1, k+1): # 从个位数开始重新排序
            buck = [[] for i in range(10)]
            for v in nums:
                item = v % (10**i) // (10**(i-1))
                buck[item].append(v) # 分桶
            nums = sum(buck, []) # 重新合并数组


        return max(nums[i+1]-nums[i] for i in range(n-1))        


    # 桶排序
    def maximumGap(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return 0
        max_v, min_v = max(nums), min(nums)
        # 如果是等差数列，则至少相距 width 个长度，因此需要记录每个桶的最大值和最小值
        # 因为答案要不就是桶宽，要不就是 相邻桶元素之间，也就是两个桶的最大值 与 最小值之间
        width = (max_v - min_v) / (n - 1) 
        if not width: return 0
        ans = [[float('inf'), -1] for i in range(n-1)] # 一共 n-1 个桶
        for i in nums:
            item = int((i-min_v-0.1) / width) # -0.1 可以保证桶的右边界也落入桶中，不落入下一个桶
            ans[item][0] = min(ans[item][0], i)
            ans[item][-1] = max(ans[item][-1], i)

        print(width, ans)
        res = int(width)
        # 处理相邻箱子的可能性
        prev = ans[0]
        i = 1
        while i < n-1:
            if ans[i][-1] == -1: # 如果某个箱子没有元素，则跳过搜寻下一个箱子
                i += 1
                continue

            res = max(res, ans[i][0]-prev[1])
            prev = ans[i]
            i += 1
        
        return res

print(Solution().maximumGap([3,6,9,1]))