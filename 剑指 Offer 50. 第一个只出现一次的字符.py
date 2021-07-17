class Solution:
    # 滑动窗口，窗口使用字典进行状态保持
    def firstUniqChar(self, s: str) -> str:
        n = len(s)
        if not n: return ' '
        if n == 1: return s[0]

        from collections import defaultdict
        window = defaultdict(int)
        slow, fast = 0, 1
        window[s[0]] = 1

        while fast < n:
            if slow == fast: 
                window[s[fast]] += 1
                fast += 1

            while fast < n and window[s[slow]] < 2:
                window[s[fast]] += 1
                fast += 1

            while slow < fast and window[s[slow]] > 1:
                slow += 1

        return ' ' if slow == n else s[slow] 
    

    # 一次遍历记录是否含有多个值，其后再次遍历找到第一个满足条件的即可
    def firstUniqChar(self, s: str) -> str:
        from collections import Counter
        total = Counter(s)
        for i in s:
            if total[i] == 1: return i
        return ' '

print(Solution().firstUniqChar(
"aaadd"))