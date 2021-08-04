class Solution:
    def lengthLongestPath(self, input: str) -> int:

        def dfs(s, k):
            # 代表没有分级的情况
            if '\n' not in s: 
                return len(s) if '.' in s else float('-inf')
            target = '\n' + '\t'*k
            n, p = len(s), len(target)
            father = 0
            prev = 0
            nxt = []
            ans = float('-inf')
            for i in range(n - p + 1):
                if s[i: i+p] == target and (i + p >= n or s[i+p] != '\t'):
                    if k and not father:
                        father = i
                    if k == 0 or prev: ans = max(ans, dfs(s[prev: i], k + 1) + father + int(k > 0) )
                    prev = i + p
            
            return max(ans, dfs(s[prev: n], k+1) + int(k > 0) + father ) 
        
        return max(0, dfs(input, 0))       

print(Solution().lengthLongestPath(
"a\n\taa\n\t\taaa\n\t\t\tfile1234567890123.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png"))