class Solution:
    def minSetSize(self, arr) -> int:
        from collections import Counter
        dic = Counter(arr)
        ans = count = 0
        threshold = len(arr) // 2
        dic = sorted(dic.values(), reverse=True)
        for i in dic:
            count += i
            ans += 1
            if count >= threshold: return ans
        

        return ans

