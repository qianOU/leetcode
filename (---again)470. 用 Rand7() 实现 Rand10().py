# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    # 最朴素的随机采样
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # 产生 [1, 49]范围内的等概率随机数
            num = (rand7() - 1)*7 + rand7()
            if num > 40: # 拒绝域
                continue
            break
        return 1 + (num - 1)% 10
    
    # 优化缩减拒绝域
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # 产生 [1, 49]范围内的等概率随机数
            num = (rand7() - 1)*7 + rand7() # 拒绝域缩减为[1,2,3,4,5,6,7,8,9]
            if num <= 40: 
                return 1 + (num - 1)% 10
            num = (num - 40 - 1)*7 + rand7() # 拒绝域缩减为[1,2,3]
            if num <= 60:
                return 1 + (num - 1)% 10
            num = (num - 60 - 1)*7 + rand7() # 拒绝域缩减为[1]
            if num <= 20: 
                return 1 + (num - 1) % 10