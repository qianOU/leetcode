class Trie: # 字典树类，实现了插入，搜索等算法

    # 字典树的节点类
    class TrieNode:
        def __init__(self): 
            self.children = defaultdict(self.__class__)
            self.ending = False # 是否作为结束的标记， 默认是否

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for w in word:
            cur = cur.children[w]
        cur.ending = True # 代表在这个节点，有单词的结束位

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        flag = True
        for w in word:
            if w not in cur.children: # 如果 w 不在 子节点之中
                flag = False
                break
            cur = cur.children[w]

        return flag and cur.ending# 以 word 最后一个单词结尾


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        flag = True
        for w in prefix:
            if w not in cur.children:
                flag = False
                break
            cur = cur.children[w]
        
        return flag