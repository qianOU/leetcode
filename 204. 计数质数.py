class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isPrimer(n):
            for i in range(2, int(n**.5)+1):
                if n%i == 0:
                    return False
            
            return True

        nums = [True] * n
        for i in range(2, int(n**.5)+1):
            if isPrimer(i):
                j = i*i
                while j < n:
                    nums[j] = False
                    j += i
        
        return sum(nums[i] for i in range(2, n))
