class Solution:
    # 滑动窗口
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        l, r = 0, 1
        ans = 0

        from collections import defaultdict
        window = defaultdict(int)
        window[s[0]] = 1

        while r < n:
            while r < n and s[r] not in window:
                window[s[r]] += 1
                r += 1
            
            ans = max(r - l, ans)

            if r >= n: break
            
            while l < r  and s[l] != s[r]:
                window[s[l]] -= 1
                if not window[s[l]]: del window[s[l]]
                l += 1
            
            if  s[l] == s[r]:
                del window[s[r]]
                l += 1
        
        return ans

print(Solution().lengthOfLongestSubstring(
"adsdqaoiwdwqrdjqhiwdfhlasdqwilrhdqwlkfdhdlfdyqweudfaskhdfgYWQueqwudfgwef"
))