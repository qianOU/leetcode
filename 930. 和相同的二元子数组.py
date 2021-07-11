class Solution:
    # 解法1： 前缀计数字典
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        presum = 0
        from collections import defaultdict
        rec = defaultdict(int)
        rec[0] = 1
        ans = 0
        for i in nums:
            presum += i
            ans += rec[presum - goal]
            rec[presum] += 1
        
        return ans
    