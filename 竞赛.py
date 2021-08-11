class Solution:
    # # 直接统计不符合规则的右括号数量
    def minSwaps(self, s: str) -> int:
        n = len(s)
        pair = count = 0
        for i in s:
            if i == ']':
                if not pair: count += 1
                else: pair -= 1
            else: pair += 1
        return count // 2 + count % 2


print(Solution().minSwaps(']]][[['))