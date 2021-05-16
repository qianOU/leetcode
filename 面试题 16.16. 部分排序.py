class Solution:
    # 基于栈 O（N）
    def subSort(self, array):
        n = len(array)
        # 两个单调栈
        left = [float('-inf')]
        right = [float('inf')]
        l, r = 0, n-1 
        max_, min_ = float('-inf'), float('inf')
        while l<=r:
            while l< n and array[l] >= left[-1]:
                left.append(array[l])
                l += 1
            # 如果左指针已经遍历完序列返回
            if l == n:
                return [-1, -1]

            while r>=0 and array[r] <=  right[-1]:
                right.append(array[r])
                r -= 1
            
            # 完整的遍历一个数组，找最小值和最大值
            while l<=r:
                max_ = max(max_, array[l])
                min_ = min(min_, array[l])
                l += 1
                

        while left[-1] > min_: # 去除之前的单调栈顶元素大于 最小值的部分
            left.pop()
        while right[-1] < max_: # 去除之前的单调递减栈顶元素 小于 最大值的部分
            right.pop()

        n1 = len(left) - 1
        n2 = len(right) - 1

        if n1 == n:
            return [-1, -1]
        else:
            return [n1 , n - n2 -1]
    
    # # 方法二： 基于排序 O(NlgN)
    # def subSort(self, array):
    #     ans = [float('inf'), float('-inf')]
    #     a = sorted((j, i) for i,j in enumerate(array))
    #     for idx, (_, origin) in enumerate(a):
    #         if idx != origin:
    #             ans[0] = min(origin, ans[0])
    #             ans[-1] = max(origin, ans[-1])
        
    #     return [-1, -1] if ans[0] == float('inf') else ans