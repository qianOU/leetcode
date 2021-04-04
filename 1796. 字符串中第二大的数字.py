class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        big = second = -1
        code = list(range(48, 58))
        for i in s:
            if ord(i) in code:
                s = int(i)
              
                if s > big:
                    second = big
                    big = s
                    
                elif  second < s < big:
                    second = s
                
                print(s, big, second)
        
        return second if big > second > -1 else  -1

print(Solution().secondHighest(
"dfa12321afd"))