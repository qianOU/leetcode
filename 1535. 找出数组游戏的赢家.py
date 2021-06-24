class Solution:
    # 计数数组 + 截断剪枝
    # 由于首先遍历数组找到最大值，再分情况讨论，这实际上是多于的可以使用，精简写法
    def getWinner(self, arr, k: int) -> int:
        n = len(arr)
        v = max(arr)
        idx = arr.index(v) # 最大值处的索引
        if k >=  idx:
            return v
        
        record = {i:j for j, i in enumerate(arr)} # 值和索引的映射表
        ans = [0]*(idx+1)
    
        res = 0
        for i in range(1, idx+1):
            arr[i] = max(arr[i-1], arr[i]) # 就地改变元素，节约空间
            ans[record[arr[i]]] += 1
            if ans[record[arr[i]]] == k:
                return arr[i]
        
        return v
    
    # 思路2: 精简写法
    def getWinner(self, arr, k: int) -> int:
        n = len(arr)
        max_v = 0
        prev = arr[0]
        cumcount = 0
        for i in arr[1:]:
            if prev < i:
                # 更新 prev 的状态，以及 计数的值置为 1
                prev = i
                cumcount = 1
            else:
                # 如果 prev 大于 curr。则 计数 + 1
                cumcount += 1
            # 记录最大值，因为一次遍历数组之后没有达到轮数k，之后就只能是 max_v了
            max_v = max(max_v, i)

            if cumcount == k:
                return prev
        
        return max_v


print(Solution().getWinner([2,1,3,5,4,6,7], 2))