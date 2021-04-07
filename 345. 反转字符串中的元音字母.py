class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)
        ans = list(s)
        d = 'aeiou'
        while left < right:
            if ans[left] in d and ans[right] in d:
                ans[left], ans[right] = ans[right], ans[left]
                left += 1
                right -= 1
            elif ans[left] in d:
                right -= 1
                continue
            elif ans[right] in d:
                left += 1
                continue
            left += 1
            right -= 1
        
        return ''.join(ans)