class Solution:
    # 字典树 + 递归超时（失败）
    # 字典树(快速查找) + 动态规划 0(n^2)
    def wordBreak(self, s: str, wordDict) -> bool:
        from collections import defaultdict

        class Trie:
            def __init__(self):
                self.word_end = False # 是否是一个单词的结尾节点
                self.childen = defaultdict(self.__class__)
            
            def insert(self, word):
                cur = self
                for w in word:
                    cur = cur.childen[w]
                cur.word_end = True
            
            def search(self, string):
                cur = self
                for j in string:
                    if j not in cur.childen:
                        return False
                    cur = cur.childen[j]
                return cur.word_end
        
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        n = len(s)
        dp = [False]*(1 + n) # dp[i] 表示的是 s[0,...i-1] 是否由提供的单词组成
        # base case
        dp[0] = True # 空字符串
        for i in range(1, n + 1):
            # 遍历最后一个单词的可能切割点
            for j in range(i-1, -1, -1):
                if dp[j] and trie.search(s[j: i]):
                    dp[i] = True
                    break 

        return dp[-1]




    # 记忆化 DFS
    def wordBreak(self, s: str, wordDict) -> bool:
        from functools import lru_cache
        n = len(s)
        record = set(wordDict)

        @lru_cache(None)
        def dfs(cur): # cur 是右开区间部分
            if  cur == 0: return True # 空字符串的时候

            # 遍历切割位置
            for cut in range(cur):
                if s[cut:cur] in record and dfs(cut):
                    return True
            return False
        
        return dfs(n)
    

    # BFS
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        from collections import deque
        q = deque([0]) 
        vis = set()
        record = set(wordDict)
        
        while q:
            cur = q.popleft() # 当前索引
            if cur == n: return True
            elif cur in vis: continue
            vis.add(cur)
            # 遍历下一个步
            for i in range(cur+1, 1 + n):
                if s[cur: i] in record:
                    q.append(i)
        return False


print(Solution().wordBreak(
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
,["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
))