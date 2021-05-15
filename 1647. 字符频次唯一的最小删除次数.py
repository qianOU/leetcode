class Solution:
    # 方法1: 不需要排序 字典 + 贪心
    def minDeletions(self, s: str) -> int:
        from collections import defaultdict
        ans = defaultdict(int)
        for i in s:
            ans[i] += 1
        
        states = ans
        count = 0
        # 从大到小删除字符
        for c in range(26):
            char = chr(c + ord('a'))
            v = ans[char]
            del ans[char]
            while v and v in ans.values():
                v -= 1
                count += 1
            ans[char] = v

        return count

    # 方法二： 数组 + 贪心， 排序
    def minDeletions(self, s: str) -> int:
        ############## 统计，排序，贪心
        freq = [0 for _ in range(26)]
        for c in s:
            freq[ord(c) - ord('a')] += 1
        freq.sort(reverse = True)

        count = 0
        # 为了确保freq的有序， 别动两者中大的元素， 而是改边较小的元素
        for i in range(1, 26):
            while freq[i] and freq[i] >= freq[i-1]:
                freq[i] -= 1
                count += 1
        
        return count