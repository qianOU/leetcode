class StockSpanner:
    # 注意是从今天开始数的最大连续递增天数，也就是找寻最近的大于当前价格的日子，跨度

    def __init__(self):
        # 单调栈
        self.stack = []
        

    def next(self, price: int) -> int:
        weight = 1 # 使用 weight 记录 到最近价格大于price 的时间跨度
        while self.stack and self.stack[-1][0] <= price: # 单调递增栈
            weight += self.stack.pop()[1]
        
        self.stack.append((price, weight)) # weight 记录的是时间跨度
        return weight
            

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)