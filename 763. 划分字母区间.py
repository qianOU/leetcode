class Solution:
    # 基于 路径记录 和 字符计数的方法。效率低
    # 可以用贪心算法，因为只和字符最后出现的位置有关
    def partitionLabels(self, s: str):
        ans = []
        n = len(s)

        from collections import Counter
        records = Counter(s)
        print(records)
        prev = -1
        path = set()
        for i in range(n):
            path.add(s[i])
            records[s[i]] -= 1
            if not any(records[i] for i in path): # 导致效果差的主要原因，事实是不需要计数，只要知道最后一个位置索引即可
                path.clear()
                ans.append(i-prev)
                prev = i

        return ans

    # 思路2 : 贪心
    def partitionLabels(self, s: str):
        ans = []
        n = len(s)
        records = [0]*26 # 只记录字符最后位置
        for i,j in enumerate(s):
            records[ord(j) - ord('a')] = i

        start = end = 0
        for i in range(n):
            # 更新结束位置
            end = max(end, records[ord(s[i]) - ord('a')])
            if i == end: # 走到片段的结束位置的时候
                ans.append(i+1-start)
                start = i + 1

                
        return ans

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))