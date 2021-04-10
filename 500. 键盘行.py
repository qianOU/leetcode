class Solution:
    def findWords(self, words) :
        a = set("qwertyuiop")
        b = set("asdfghjkl")
        c = set("zxcvbnm")
        return list(filter(lambda x: any(set(x.lower()).issubset(i) for i in [a,b,c]), words))


print(Solution().findWords( ["Hello","Alaska","Dad","Peace"]))