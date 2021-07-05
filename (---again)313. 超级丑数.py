class Solution:
    # 质因数指的就是 因数全部都是 质数 的数
    # 263 是判断数字是否是丑数，这道题是扩增丑数， 丑数的质因子都在 primes 中，也就是 primes中的组合相乘    
    # 思路1： 使用小根堆（没有使用 primes 的有序性， 递增的有序性通过堆来维护）
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq
        heap = [1] # 1 是丑数的初始值
        heapq.heapify(heap)

        for i in range(n):
            prev = heap[0]
            # 确保每次取出来的都是不同的丑数，（去除相同值）
            while heap and prev == heap[0]:
                heapq.heappop(heap)
            # 乘以每一个质因子, 入堆
            for j in primes:
                heapq.heappush(heap, j*prev)
        
        return prev
    

    # 思路2： 动态规划
    # 与 264 思路一致，不过由于质因子的不同，指针数目也是不定的，使用指针字典来维护
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0]*(n+1) # dp[i] 表示第 i 个 丑数
        # base-case
        dp[1] = 1

        # 指针字典
        p_ = {i: 1 for i in primes}

        for i in range(2, n+1):
            nex = min(dp[p_[k]]*k for k in primes)
            dp[i] = nex
            for k in p_:
                if dp[p_[k]]*k == nex:
                    p_[k] += 1
        
        return dp[-1]