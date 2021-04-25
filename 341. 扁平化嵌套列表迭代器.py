# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [] # 倒序入栈,意味着正序出栈
        for i in range(len(nestedList)-1, -1, -1):
            self.stack.append(nestedList[i])
    
    def next(self) -> int:
        if self.hasNext():
            top = self.stack.pop()
            return top.getInteger()
    
    # 使用 next 之前,测试案例会调用 hasNext, 所以对于哪些空列表需要使用 hasNext 进行对比
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            # 如果是列表,继续倒序入栈
            else:
                top = self.stack.pop().getList()
                for i in range(len(top)-1, -1, -1):
                    self.stack.append(top[i])
        
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())