# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        presign = '+'
        n = len(s)
        num = 0
        is_num = False
        if s[0] != '[':
            return NestedInteger(int(s))

        for i in range(n):
          
            s1 = s[i]

            if s1 == '[': # 产生新的嵌套对象
                stack.append(NestedInteger())

            elif s1.isdigit():
                num = num * 10 + int(s1)
                is_num = True # 确定是产生数字的标识
            
            elif s1 in '],-':
                if presign == '+':
                    item = NestedInteger(num)
                else:
                    item = NestedInteger(-num)
                if is_num:
                    stack[-1].add(item)
                               
                if s1 == '-':
                    presign = s1
                else:
                    presign = '+'
                
                num = 0
                is_num = False

            # 形成嵌套关系
            if s1 == ']' and len(stack) > 1:
                item = stack.pop()
                stack[-1].add(item)
            
            

        return stack[0]