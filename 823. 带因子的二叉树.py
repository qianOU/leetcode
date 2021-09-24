class Solution:
    # 因子分解
    def numFactoredBinaryTrees(self, arr) -> int:
        base = 10**9 + 7
        n = len(arr)
        arr.sort()
        map_ = {j: i for i, j in enumerate(arr)} # 映射表
        dp = [1]*n
        ans = 0
        hasdone = [False] * n
        for idx, i in enumerate(arr):
            for r in range(map_[i]):
                item, res = divmod(i, arr[r])
                if res == 0 and item in map_:
                    l = map_[item]
                    dp[idx] = (dp[idx] + dp[l] * dp[r]) % base
                
        return sum(dp) % base

print(Solution().numFactoredBinaryTrees(
[45,42,2,18,23,1170,12,41,40,9,47,24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43,15,4,16,35,25,20,44,5,48]
))