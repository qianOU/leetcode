class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        prev = cur = 1

        for i in range(1, n):
            if  0<= arr[i] - prev <= 1:
                cur = arr[i]
            else:
                cur += 1
            prev = cur 
        
        return cur