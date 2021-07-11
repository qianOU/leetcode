class Solution:
    # O(N**2) TSL
    def totalHammingDistance(self, nums: List[int]) -> int:
        
        memory = {}
        def dfs(a, b):
            ask = (min(a, b), max(a, b))
            if memory.get(ask, None) is not None:
                return memory[ask]
            ans = 0
            item = a ^ b
            while item:
                ans += item & 1
                item >>= 1

            memory[ask] = ans
            return memory[ask]

        ans = 0
        n = len(nums)
        # 使用了 O(N2)的枚举复杂度
        for i in range(n):
            for j in range(i+1, n):
                ans += dfs(nums[i], nums[j])
        
        return ans

    # 由于 ，每两个数的每个 bit 位 都会进行比较，所以从 bit 位的统计结果出发
    def totalHammingDistance(self, nums: List[int]) -> int: 
        n = len(nums)
        ans = 0
        for i in range(30):
            item = 0 # 第 i 个 bit 位，有多少个 1
            for num in nums:
                item += (num >> i) & 1
            # 由于是排列需要考虑顺序
            ans += item * (n - item)
        return ans


