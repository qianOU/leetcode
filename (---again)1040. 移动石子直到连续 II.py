class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        mx = max(stones[n-1]-stones[1]+2-n, stones[n-2]-stones[0]+2-n)
        mix = mx
        i = j = 0
        for  i in range(n):
            while j+1 < n and stones[j+1] - stones[i] + 1 <= n:
               j += 1
            cons = j - i + 1 # 在 i的 n 范围内 一共有 j = i + 1 个点
            if  j - i + 1 == n-1 and stones[j] - stones[i] + 1 == n-1:
                cons = 2
            mix = min(mix, cons)
            i = j
        
        return [mix, mx]