class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        arr = [[n]*n for i in range(n)]
        ans = 0
        for i, j in mines:
            arr[i][j] = 0
        
        for k in range(n): # 同时循环 k 行 and k 列
            l = r = u = b = 0 # 最大臂长记录
            for i, j in zip(range(n), range(n-1, -1, -1)):# 从上下左右四个方向进行搜索记录最大臂长
                l = l + 1 if arr[k][i] else 0
                arr[k][i] = min(arr[k][i], l) # 左 ---> 右
                
                r = r + 1 if arr[k][j] else 0
                arr[k][j] = min(arr[k][j], r) # 右 ---> 左

                u = u + 1 if arr[i][k] else 0
                arr[i][k] = min(arr[i][k], u) # 上 --> 下

                b = b + 1 if arr[j][k] else 0
                arr[j][k] = min(arr[j][k], b) # 从 下 ---> 上
            
        return max(max(i) for i in arr)

        

