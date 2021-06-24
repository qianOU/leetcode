class Solution:
    # 思路1： 贪心  + 红黑树 (效率低)
    def prevPermOpt1(self, arr):
        n = len(arr)
        res = [arr[-1]]*n
        from sortedcontainers import sortedlist
        a = sortedlist()
        records = {}
        for i in range(n-1, -1, -1):
            idx = a.bisect_left(arr[i]) # 找到 小于等于 i 的最大元素
            a.append(arr[i])
            records[arr[i]] = i
            if idx == 0: continue
            else:
                arr[i], arr[records[arr[idx-1]]] = arr[records[arr[idx-1]]], arr[i]
                return arr

    # 大佬思路： 双指针 + 贪心
    # 从右往左遍历，找寻 离right最近的左边元素，其值大于 arr[right] 记为 left， 交换位置   
    def prevPermOpt1(self, arr):
        n = len(arr)
        left = right = float('-inf') 

        for i in range(n-1, 0, -1):
            if i <= left: break # left 是找到的交换的最高位， 如果 i <= left 则得到的结果不是第二大的
            for j in range(i-1, -1, -1):
                if arr[j] > arr[i]:
                    if j > left: # 剪枝
                        left = j
                        right = i
                        break # 找到对于 i 来说， 离其最近的并且满足条件的可能的解

                elif arr[j] == arr[i]: # 如果这种情况发生，则对于 i 的搜索可以停止，剪枝
                    break
        
        if left > float('-inf'):
            arr[left], arr[right] = arr[right], arr[left]
        return arr
