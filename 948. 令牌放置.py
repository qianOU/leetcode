class Solution:
    #暴力 + 回溯
    def bagOfTokensScore(self, tokens, power: int) -> int:
        tokens.sort()
        n = len(tokens)
        l, r = 0, n - 1
        max_ = 0

        def back_track(l, r, p, s):
            nonlocal max_
            # base-case
            if  l>r :
                max_ = max(max_, s)
                return 
            
            # 选择1
            if p-tokens[l] >= 0:
                back_track(l+1, r, p-tokens[l], s+1)
            else: # 无法进行令牌移动的时候，得到能获取的最大值
                max_ = max(max_, s)
            # 选择2
            if s > 0:
                back_track(l, r-1, p+tokens[r], s-1)

        back_track(0, n-1, power, 0)

        return max_
    
    # 方法二： 贪心 每次只有能量不够用的时候才 减少分数 换取能量
    def bagOfTokensScore(self, tokens, power: int) -> int:
        tokens.sort()
        n = len(tokens)
        l, r = 0, n - 1
        score = 0

        while l <= r:
            while l < n and power >= tokens[l]:
                power -= tokens[l]
                l += 1
                score += 1
            if score > 0 and l < r and power + tokens[r] >= tokens[l]:
                power += tokens[r]
                r -= 1
                score -= 1
            else:
                break
        
        return score

print(Solution().bagOfTokensScore([48,87,26],
81))