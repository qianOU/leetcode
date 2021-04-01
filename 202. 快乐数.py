class Solution(object):
    # 也可以使用快慢指针技巧 /判断循环是否存在都可以使用快慢指针技巧/
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        visited.add(n)
        total = n
        while total!=1:
            sum_ = 0
            while n:
                m = n % 10
                n //= 10
                sum_ += m**2
            n = sum_
            if sum_ == 1:
                return True
            if sum_ in visited:
                return False
            visited.add(sum_)
        return True

    # 快慢指针
    def isHappy2(self, n):
        def nextone(n):
            sum_ = 0
            while n:
                m = n % 10
                sum_ += m**2
                n //= 10
            return sum_
        
        slow = n # slow 每次只进行一次计算
        fast = n # fast 需要多做一次计算

        while True:
            slow = nextone(slow)
            fast = nextone(fast)
            fast = nextone(fast)

            if slow == fast:
                break
        
        return slow == 1

A = Solution()
print(A.isHappy2(19))