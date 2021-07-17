class Solution:
    # 线性 一次扫描
    def minArray(self, numbers: List[int]) -> int:
        ans = numbers[0]
        n = len(numbers)
        for i in range(1, n):
            if numbers[i] - numbers[i-1] < 0:
                ans = numbers[i]
                break
        return ans
    
    # 二分
    def minArray(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers)-1

        while l < r:
            mid = l + (r - l) // 2
            # 如果不能区分左半区间还是右半区间有序的话，就同时缩放左右边界
            # 因为 numbers[mid] 的存在，所以可以缩放等值的 l 和 r 
            if  numbers[l] == numbers[mid] == numbers[r]:
                l += 1
                r -= 1
            # mid 小于等于 numbers[r] ， 表明 mid 也可能是想找寻的 最小值点，所以右边界锁定为 r
            elif numbers[mid] <= numbers[r]: 
                r = mid
             # mid 大于等于numbers[l] ， 表明 mid 不可能是想找寻的 最小值点
            elif numbers[mid] >= numbers[l]:
                l = mid + 1
            

        return numbers[l]


    # 二分: 优美的写法
    def minArray(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers)-1

        while l < r:
            mid = l + (r - l) // 2
            # mid 小于 numbers[r] ， 表明 mid 也可能是想找寻的 最小值点，所以右边界锁定为 r
            if numbers[mid] < numbers[r]: 
                r = mid
            # 如果有重复元素，并且 numbers[mid] == numbers[r]，则可以放心的删除 r 对应的值
            elif numbers[mid] == numbers[r]:
                r -= 1
            # mid 落在有序的左半区间
            else:
                l = mid + 1
          
        return numbers[l]