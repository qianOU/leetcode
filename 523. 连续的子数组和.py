class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        n = len(nums)
        presum = 0
        from collections import defaultdict
        rec = set([0])
        bef = prev = None

        for i in range(n):

            presum += nums[i]
            # 处理 0 始终 视为 k 的一个倍数的情况，即连续出现两个0的情况
            print(i, presum, prev, bef)
            if presum == bef: return True
            elif presum > 0 and presum % k == 0: return True
            for j in range(1, presum // k + 1):
                if presum - j*k in rec:
                    print(rec, presum, j )
                    return True

            bef = prev
            prev = presum
            
            rec.add(presum)

        return False


print(Solution().checkSubarraySum(
[23,2,0,0,6],
7
))