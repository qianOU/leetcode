class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = [float('inf')] # 记录每一次插入的时候的栈内的最小值
        self.stack = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.min.append(val if val < self.min[-1] else self.min[-1])
        self.stack.append(val)



    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]

