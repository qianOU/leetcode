class Solution:
    # 方法 1 ： 递归模拟， 需要对数组进行操作交换元素
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def search_max(left, right):
            idx = left
            for i in range(left, right):
                if arr[idx] < arr[i]:
                    idx = i
            
            return idx
        
        ans = []
        def dfs(left, right): # 左闭右开的递归区间
            if left >= right:
                return 
            
            idx = search_max(left, right)

            if idx == right - 1: # 如果最大数已经是在最后以为的时候
                return dfs(left, right-1)

            if idx:
                ans.append(idx+1)
                i, j = left, idx
                while i < j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
                
                dfs(left, right) # 将最大数换到第一位，进行下一层转换
            else: # 最大数在第一位的时候
                ans.append(right)
                i, j = idx, right-1
                while i < j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
                dfs(left, right-1) # 将第一位的最大值，移动到最末尾，所以这里要缩尾

            
        
        dfs(0, len(arr))

        return ans


    # 方法 2:  基于迭代的方法 不对数组元素进行交换
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n  = len(arr)
        # 排序获得 arr 中最大值 处于 的 索引位置 + 1 的 值
        B = sorted(range(1, n+1), key = lambda i: -arr[i-1])

        for i in B: # 遍历顺序，代表 优先处理 数组的最大值
            for f in ans: # 对于 arr[i-1] 而言，我们需要找到在 倒置多次后，真实的 arr[i-1] 的位置
                if i <= f:
                    i = f + 1 - i # 这是交换规则，画图可以有助于理解
            ans.extend([i, n])
            n -= 1 
        
        return ans