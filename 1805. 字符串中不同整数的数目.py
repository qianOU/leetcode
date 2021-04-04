class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """

        fast = 0
        n = len(word)
        ans = set()

        tmp = ''
        while fast < n:
            if word[fast].isdigit():
                tmp+=word[fast]
                fast += 1
                continue
            print(tmp)
            if tmp:
                ans.add(int(tmp))
                tmp = ''
            fast += 1
        
        if tmp:
            ans.add(int(tmp))
        
        print(ans)
        return len(ans)

print(Solution().numDifferentIntegers("leet1234code234"))