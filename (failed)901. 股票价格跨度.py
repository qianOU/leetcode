class StockSpanner:

    def __init__(self):
        # 单调栈
        self.stack = [(float('-inf'), 0)]
        

    def next(self, price: int) -> int:
        while  self.stack[-1][0] <= price: # 单调递增栈
            self.stack.pop()
            flag = 1 # 删除了部分元素
        
        if not flag:
            self.stack.append(1 + self.stack[-1][-1])
        else:
            self.stack.append(self.stack[-1][-1])
        
        return self.stack[-1][-1]
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)