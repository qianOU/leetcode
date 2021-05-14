class Solution:
    def smallestK(self, arr, k: int) :
        import random
        # 基于随机单部分快排思想
        def random_quick(start, end, k): # 左闭右闭区间
            if start > end:
                return

            idx = random.randint(start, end)
            K = arr[idx]
            arr[idx], arr[end] = arr[end], arr[idx]
            
            # [start,  ... l] 都是小于等于 K的
            l = start - 1
            for i in range(start, end):
                if arr[i] <= K:
                    l += 1
                    arr[l], arr[i] = arr[i], arr[l]
            
            l += 1
            arr[l], arr[end] = arr[end], arr[l]

            if l - start + 1 > k:
                return random_quick(start, l-1, k)
            elif l-start+1 < k:
                return random_quick(l+1, end, k - l + start-1)
        
        random_quick(0, len(arr)-1, k)

        return arr[:k]


print(Solution().smallestK([1,3,5,7,2,4,6,8], 4))