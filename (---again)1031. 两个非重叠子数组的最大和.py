class Solution:
    # 滑动窗口， 一个窗口同时维护三个状态，Max, maxL, maxM
    # 两种情况， L数组在前， 或者 M 数组在前
    def maxSumTwoNoOverlap(self, nums, firstLen: int, secondLen: int) -> int:
        presum = [0] # 前缀和
        n = len(nums)
        for i in nums:
            presum.append(presum[-1] + i)

        L, M  = firstLen, secondLen
        Max, maxL, maxM = presum[L+M], presum[L], presum[M]

        print(Max, maxL, maxM )
        for i in range(L+M, n+1):
            # 更新 L在前时的最大值
            maxL = max(maxL, presum[i-M] - presum[i-L-M])
             # 更新 M在前时的最大值
            maxM = max(maxM, presum[i-L] - presum[i-L-M])

            Max = max(Max,
                max(
                   # 前期 L的最大值，与当前 M 期的组合的最大值
                   maxL + presum[i] - presum[i-M],
                   # 前期  M的最大值，与当前 L 期的组合的最大值
                   maxM + presum[i] - presum[i-L] 
                ))
            
            print(Max, maxL, maxM )

        return Max




print(Solution().maxSumTwoNoOverlap(
[2,1,5,6,0,9,5,0,3,8],
4,
3
))