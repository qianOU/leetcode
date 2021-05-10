class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        # 就地排序， 快排
        def quick(left, right): # 左闭右开
            #base-case
            if left >= right:
                return

            k = arr[left]
            l = left + 1
            r = right - 1
            # 搜索区间为左闭右闭
            while l <= r:
                while l < right and arr[l] < k:
                    l += 1
                while r >= 0 and arr[r] > k:
                    r -= 1
                
                if l >= r:
                    break
                
                arr[l], arr[r] = arr[r], arr[l]
                # Note
                l, r = l+1, r-1 # 交换之后需要 l， r 移动，不然在面对 arr[l] == arr[r] == k时，会陷入死循环
            
            arr[left], arr[r] = arr[r], arr[left]

            quick(left, r)
            quick(l, right)

        m, n = len(mat), len(mat[0])

        for k in range(n):
            arr = []
            idx = 0
            for i in range(m):
                j = i + k
                if j < n:
                    arr.append(mat[i][j])
            
            for i in range(m):
                j = i + k
                if j < n:
                    mat[i][j] = arr[idx]
                    idx += 1
        
        return mat
                    
