class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        n = len(arr)
        cur = None
        for i in range(n-1):
            if cur and arr[i+1] - arr[i] != cur:
                return False
            if not cur:
                cur = arr[i+1] - arr[i]
        
        return True