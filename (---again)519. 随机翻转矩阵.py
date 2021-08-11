class Solution:
    # 拒绝采样，可能需要调用多次的 random 
    def __init__(self, m: int, n: int):
        self.visited = set()
        self.m, self.n = m, n

    def decode(self, x):
        return [x // self.n, x % self.n]
    
    def encode(self, x, y):
        return self.m * x + y

    def flip(self) -> List[int]:
        code = random.randint(0, self.m*self.n - 1)
        while code in self.visited:
            code = random.randint(0, self.m*self.n - 1)
        self.visited.add(code)
        return  self.decode(code)


    def reset(self) -> None:
        self.visited.clear()


class Solution:
    # 优化，每次 flip 只调用一次 random
    # 每次抽取无效的元素索引k，放到尾部，同样的将尾部有效的值来替换当前抽样的索引k，这就保证了在[0, num-1] 都是符合题意的0
    def __init__(self, m: int, n: int):
        self.lookup = dict()
        self.origin = self.num = n * m - 1
        self.n = n

    def flip(self) -> List[int]:
        idx = code = random.randint(0, self.num)
        if code in self.lookup:
            code = self.lookup[code]
        self.lookup[idx] = self.lookup.get(self.num, self.num) # 尾部元素挪到前面
        self.num -= 1 # 收缩 k
        return [code//self.n, code % self.n]


    def reset(self) -> None:
        self.lookup.clear()
        self.num = self.origin
# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()