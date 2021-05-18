class Solution:
    def partition(self, s: str):
        n = len(s)
        ans = []

        def dfs(i, path):
            if i >= n:
                if path[-1] == path[-1][::-1]:
                    ans.append(path.copy())
                return 
            # 选择 1： 
            if path[-1] == path[-1][::-1]: # 如果前一个子字符串已经构成回文序列
                dfs(i+1, path+[s[i]])

            # 选择 2： 当前字符和前一个字符串合并，组成后序的回文串
            item = path[-1] + s[i]
            path[-1] = item
            dfs(i+1, path) 
    
        dfs(1, [s[0]])
        
        return ans

print(Solution().partition('efe'))