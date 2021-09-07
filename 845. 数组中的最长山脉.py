class Solution:
    # 朴素思路 
    def longestMountain(self, arr) -> int:
        n = len(arr)
        res = [1]*n
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                res[i] = res[i-1] + 1
        
        tmp = [1]*n
        for r in range(n-2, 0, -1):
            if arr[r] > arr[r+1]:
                tmp[r] = tmp[r+1] + 1
        ans = 0
        print(res)
        print(tmp)
        for i, j in zip(res, tmp):
            if i > 1 and j > 1 and i + j - 1 >= 3: # 有上升区间也有下降区间
                ans = max(ans,  i + j - 1)
        return ans

print(Solution().longestMountain([0,1,2,3,4,5,6,7,8,9]))