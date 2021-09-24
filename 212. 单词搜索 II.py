class Trie:
    def __init__(self):
        self.children = defaultdict(self.__class__)
        self.end = False
        self.char = ''

    def insert(self, word):
        cur = self
        for w in word:
            cur = cur.children[w]
            cur.char = w
        cur.end = True

from collections import defaultdict

# 字典树 + BFS
# 找到某一个字符串后，并且其无后继节点的时候，删除该节点
class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        total = []
        
        def dfs(x, y, cur, path):
            item = path + cur.char
            print(x, y, cur.char, path)
            if cur.end and not cur.children: 
                total.append(item)
                return True

            for i, j in d:
                x1, y1 = x + i, y + j
                if 0 <= x1 < m and 0 <= y1 < n and cur.children.get(board[x1][y1]):
                    flag = dfs(x1, y1, cur.children[board[x1][y1]], item)
                    if flag:
                        cur.children.pop(board[x1][y1]) # 后序删除

            return not cur.children
        
        trie = Trie()
        for word in words: trie.insert(word)
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.children[board[i][j]], '')
        return total

print(Solution().findWords(

[["a","b","e"],["b","c","d"]],
["abcdeb"]
))