class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map_ = dict(zip("([{", ")]}"))
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                one = stack.pop()
                if i != map_[one]:
                    return False
        return True if len(stack) == 0 else False

A =  Solution()
print(A.isValid(")"))