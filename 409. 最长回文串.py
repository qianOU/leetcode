class Solution:
    # 动态规划
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        a =  Counter(s)
        sum_ = 0
        for _, j in a.items():
            if j%2==0:
                sum_ += j
        return sum_ + 1 if len(s)%2 else sum_