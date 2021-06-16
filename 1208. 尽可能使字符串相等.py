class Solution:
    # 滑动窗口
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = []
        for i in range(n):
            cost.append(abs(ord(s[i]) - ord(t[i])))
        
        print(cost)
        # 滑动窗口在 cost 里面 找寻最大长度的窗口，在 window_cost <= maxCost 的前提之下
        window = ans = 0
        l = r = 0 # 序列的左边界
        while r < n:
            if window + cost[r] <= maxCost:
                print(l, r, window)
                window += cost[r]
                ans = max(ans, r - l + 1)
                r += 1
            else: 
                window -= cost[l]
                l += 1
    
        return ans


print(Solution().equalSubstring(
"ujteygggjwxnfl",
"nstsenrzttikoy",
43
))