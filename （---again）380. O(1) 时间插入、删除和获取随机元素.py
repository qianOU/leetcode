# 用数组储存元素，保证了 随机选择 以及 插入的 0（1） 复杂度，在数组末尾删除，也可以保证 删除的时间复杂度
# 用字典保存 值 ---> 索引 的映射，保证了 查询的 时间复杂度
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = [] # 0(1) 时间插入
        self.dic = dict() # O(1) 索引查询 以及 0(1) 是否存在
        self.n = -1 # 数组最后一个元素的索引


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic:
            return False
        self.n += 1
        self.store.append(val)
        self.dic[val] = self.n
        
        return True

    # 保证数组删除的时间的复杂度是一大亮点！！！
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dic:
            return False
        # 将要删除的元素，交换到数组尾部，之后再执行删除，这就确保了时间复炸度为 0（1）
        idx = self.dic[val]
        self.dic[self.store[self.n]] = idx # 更新字典，将最后一个元素的移动到 要删除的 位置
        self.store[idx], self.store[self.n] = self.store[self.n], self.store[idx]
        
        self.n -= 1
        self.store.pop()
        del self.dic[val]
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, self.n)
        return self.store[idx]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()