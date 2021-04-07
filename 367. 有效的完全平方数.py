class Solution:
    # 二分搜索
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left <= right:
            mid = left + int((right-left)/2)
            tmp = mid**2
            if tmp < num:
                left = mid+1
            elif tmp > num:
                right = mid - 1
            else:
                return True
        return False

    # 基于二分搜索，通过分析实际上可以进行优化
    def isPerfectSquare(self, num: int) -> bool:
        # 优化左边界 从 2开始
        if num < 1:
            return False
        left = 2  
        right = num // 2 # 将右边界进行压缩，减少遍历的次数
        while left <= right:
            mid = left + (right-left) // 2
            tmp = mid**2
            if tmp < num:
                left = mid+1
            elif tmp > num:
                right = mid - 1
            else:
                return True
        return False
    
    # 基于牛顿迭代法
    def isPerfectSquare(self, num: int) -> bool:
 
        # 设置初始值
        x = num//2 # 是合理的，因为 1，2，3，这 三个数都不会经过 while 循环， 而 >= 4的部分的平方根一定是 小于等于 num//2 的
        while x**2>num:
            x = int(x/2 + num/2/x)
        print(x)
        return x**2 == num     

print(Solution().isPerfectSquare(101))