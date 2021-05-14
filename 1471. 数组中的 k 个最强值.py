class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        mid = (n-1)//2

        isright = lambda l, r:  arr[r] - arr[mid] > arr[mid] - arr[l] or (arr[r] - arr[mid] == arr[mid] - arr[l] and arr[r] > arr[l])
        ans = []
        left, right = 0, n-1
       
        for i in range(k):
            if isright(left, right):
                ans.append(arr[right])
                right -= 1
            else:
                ans.append(arr[left])
                left += 1
        
        return ans
