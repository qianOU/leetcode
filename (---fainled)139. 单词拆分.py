class Solution:
    # 字典树 + 前缀树
    def wordBreak(self, s: str, wordDict) -> bool:
        from collections import defaultdict

        class Trie:
            def __init__(self):
                self.word_end = 0 # 是否是一个单词的结尾节点
                self.childen = defaultdict(self.__class__)
            
            def insert(self, word):
                cur = self
                for w in word:
                    cur = cur.childen[w]
                cur.word_end = 1
            
            def search(self, string, i):
                cur = self
                res = []
                for j in range(i, len(string)):
                    if cur.childen.get(string[j]):
                        cur = cur.childen.get(string[j])
                        if cur.word_end:
                            res.append(j+1)
                    else: 
                        # 如果有这个单词返回 待匹配长句的 下一个匹配起始处， 否则放回 0 
                        return res
               
                return [j+1] if cur.word_end else res

        def search(trie, s, res):
            
            # print(s, res)
            m = len(res) # 倒序遍历，优先匹配大字符串
            n = len(s)
            print(n, res)
            for idx in range(m-1, -1, -1):
                beg = res[idx]
                # print(beg, n)
                if beg >= n: return True
                nxt = trie.search(s, beg)
                if search(trie, s, nxt): 
                    return True
            
            return False

        
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        print(1)
        
        return search(trie, s, [0])

print(Solution().wordBreak(
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
,["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
))