class Solution:
    # 快排 topk 问题
    def getLeastNumbers(self, arr, k: int):

        def top_k(left, right, k): # 闭区间
            if left <= right: return
            mid = random.randint(left ,right)
            arr[mid], arr[right] =  arr[right], arr[mid]

            prev = left - 1
            for l in range(left, right):
                if arr[l] < arr[right]:
                    prev += 1
                    arr[prev], arr[l] = arr[l], arr[prev]
            
            prev += 1
            arr[prev], arr[right] = arr[right], arr[prev]

            if prev - left + 1 == k:
                return 
            elif prev - left + 1 > k:
                top_k(left, prev - 1, k)
            else:
                top_k(prev + 1, right, k - (prev - left + 1))
        
        top_k(0, len(arr) - 1, k)

        return arr[:k]
