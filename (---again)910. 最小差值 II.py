class Solution:
    # 巧妙的贪心思路（其实就是找一个中间点 i， 将 i 左侧的所有元素 + K, 将 i 的右侧的所有元素 - K）
    # 确定可能的最值
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tmp = sorted(nums)
        ans = tmp[-1] - tmp[0]

        for i in range(n-1):
            ans = min(ans,
                max(tmp[i] + k, tmp[-1] - k) - min(tmp[0] + k, tmp[i+1] - k)
                )
        return ans
