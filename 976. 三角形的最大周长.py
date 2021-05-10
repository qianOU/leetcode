class Solution:
    # 暴力方法，没有思考隐含条件
    def largestPerimeter(self, nums: List[int]) -> int:
        arr = sorted(nums, reverse=True)
        n = len(arr)
        for i in range(n-2):
            for j in range(i+1, n-1): # 实际上要求周长最大也就限制了 j = i+1，
                for h in range(j+1, n): # 实际上要求周长最大也就限制了 h= j+1，
                    if arr[h] + arr[j] > arr[i]:
                        return arr[h] + arr[j] + arr[i]
                    else:
                        break
                
                    
        
        return 0
        
    # 方法二： 基于贪心的暴力法： 因为要找寻最大周长三角形，因此只要考虑连续的三个数是否符合三角形存在的条件即可
    # 构成三角形只要两个最短边只和大于最长边即可，而要求周长最长也就意味着两个最短边要尽可能长，也就是 i 的 后两位
    def largestPerimeter(self, nums: List[int]) -> int:
        arr = sorted(nums, reverse=True)
        n = len(arr)
        for i in range(n-2):
            if arr[i+1] + arr[i+2] > arr[i]:
                return arr[i+1] + arr[i+2] + arr[i]
        
        return 0