class Solution:
    def optimalDivision(self, nums) -> str:
        
        # 返回 [lb, rb] 区间内的 [最小值，最大值，最小值表达式，最大值表达式]
        def dfs(lb, rb):
            if lb == rb: return [nums[lb], nums[rb], str(nums[lb]), str(nums[rb])]
            #  [lb, rb] 区间内的 [最小值，最大值，最小值表达式，最大值表达式]
            res = [float('inf'), float('-inf'), '', '']
            for i in range(lb, rb): # 遍历所有可能的除号位置
                left = dfs(lb, i) # 除号的左部分
                right = dfs(i+1, rb) # 除号的右部分
                if res[0] > left[0] / right[1]: # 左半部分最小值 / 右半部分最大值
                    res[0] = left[0] / right[1] 
                    # 如果右半区间只有一个元素则不需要加 括号
                    res[2] = left[2] + '/' + ('(' if i+1 != rb else '') + right[3] + (')' if i+1 != rb else '')
                if res[1] < left[1] / right[0]:
                    res[1] = left[1] / right[0]
                    res[-1] = left[-1] + '/' + ('(' if i+1 != rb else '') + right[2] + (')' if i+1 != rb else '')
            
            return res
        
        return dfs(0, len(nums) - 1)[-1]
    
    # 数学解法, 以第一个除号为分界
    def optimalDivision(self, nums) -> str:
        n = len(nums)
        if n == 1: return str(nums[0])
        return str(nums[0]) + '/' + ('(' if n > 2 else '') + '/'.join(str(i) for i in nums[1:]) +  (')' if n > 2 else '') 
