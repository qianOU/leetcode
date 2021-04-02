class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
        self.b = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.a.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for i in range(len(self.a)-1):
            self.b.append(self.a.pop(0))

        temp  = self.a.pop()
        # 恢复 a 队列
        for i in range(len(self.b)):
            self.a.append(self.b.pop(0))
        return temp


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        for i in range(len(self.a)-1):
            self.b.append(self.a.pop(0))

        temp  = self.a.pop()
        self.b.append(temp)
        # 恢复 a 队列
        for i in range(len(self.b)):
            self.a.append(self.b.pop(0))
        return temp


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.a) == 0



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
for i in range(1)
obj.push(x)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()