import random
arr = [4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5]
# arr = arr[:100]
def quick(start, end): # 左闭右开区间
        # print(arr[start:end], start, end)
        if end <= start:
            return 

        k = arr[start] # base 元素
        
        # 左闭右闭区间
        left = start + 1
        right = end - 1
        
        while left <= right:
            while  left < end and arr[left] <= k:
                left += 1

            while right >=0 and arr[right] > k:
                right -= 1

            if left > right:
                break
            
            arr[left], arr[right] = arr[right], arr[left]
  

        arr[start], arr[right] = arr[right], arr[start]

        quick(start, right) 
        quick(left, end)

def quick(left, right): # 左闭右开
            if right <= left:
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
                
                arr[l], arr[r] = arr[r], arr[l] # 交换之后需要 l， r 移动，不然在面对 arr[l] == arr[r] == k时，会陷入死循环
                l += 1
                r -= 1

            arr[left], arr[r] = arr[r], arr[left]

            quick(left, r)
            quick(l, right)

quick(0, len(arr))
# print(arr)


def quick_select(l, r, target):
    import random

    if l > r:
        return 
    mid = random.randint(l, r)
    K = nums[mid]
    nums[mid], nums[r] = nums[r], nums[mid]
    lo = l
    hi = r - 1
    count = -1
    while lo <= hi:
        if lo <= hi and nums[lo] <= K:
            lo += 1
        elif lo<=hi and nums[hi] < K:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            hi -= 1
        else:
            hi -= 1
    
    nums[lo], nums[r] = nums[r], nums[lo]
    if lo - l + 1 == target:
        return nums[lo]
    elif lo - l + 1 > target:
        return quick_select(l, lo-1, target)
    else:
        return quick_select(lo+1, r, target-lo+l-1)

nums = list([1,2,3])

print(quick_select(0, len(nums)-1, (len(nums)+1)//2+1))


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        from functools import cmp_to_key
        n = len(nums)
        res = [[] for i in range(n)]
        for i in range(n):
            res[i].extend(nums[max(0, i-k):min(n, k+i+1)])
            a = min(res[i], key=cmp_to_key(lambda x, y: abs(x-y)))
            print(res[i], a)
            if a <= t:
                return True
        
        return False

print(Solution().containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))