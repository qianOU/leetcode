class Solution:
    #  DFS
    def findLUSlength(self, strs) -> int:
        strs.sort(key=lambda x: (len(x), x), reverse=True)
        n = len(strs)

        def check(str1, str2): # 检测 str2 是否搜 str1 的子序列
            p2 = 0
            len2 = len(str2)
            for i in str1:
                if i == str2[p2]: p2 += 1
                if p2 == len2: return True
            return p2 == len2

        visited = set()
        l = 0
        for i in range(1, n+1):
            if i==n or strs[i] != strs[l]:
                if i == l+1 and not any(check(org, strs[l]) for org in visited): 
                    return  len(strs[l])
                visited.add(strs[l])
                l = i
        
        return -1

print(Solution().findLUSlength(["aabbcc", "aabbcc","c"]))