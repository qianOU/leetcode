class CustomStack:

    def __init__(self, maxSize: int):
        self.ans = ['']*maxSize
        self.max = maxSize
        self.len = 0


    def push(self, x: int) -> None:
        if self.len < self.max:
            self.ans[self.len] = x
            self.len += 1

    def pop(self) -> int:
        if self.len == 0:
            return -1
        else:
            self.len -= 1
            return self.ans[self.len-1]

    def increment(self, k: int, val: int) -> None:
        for i in range(self.len):
            if i >= k:
                return 
            self.ans[i] += val




# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)