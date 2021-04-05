class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        set_ = set(words)
        set_.add('')
        def isvalid(i):
            while len(i) > 0:
                if i not in set_:
                    return False
                i = i[:-1]
            return True
        items = iter(sorted(words, key = lambda x: (len(x), [122-ord(i) for i in x]), reverse=True))
        for i in items:
            if isvalid(i):
                return i
        
print(Solution().longestWord(["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]))