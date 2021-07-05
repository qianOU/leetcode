# Fisher 洗牌算法
class Solution:

    def __init__(self, nums: List[int]):
        self.orignal =  list(nums)
        self.array = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = list(self.orignal)
        return self.array


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.array)
        import random
        
        for i in range(n):
            idx = random.randint(i, n) # 在 [i,...n-1] 位置中，找寻一个交换位置和 i 的位置值进行交换
            self.array[i], self.array[idx] = self.array[idx], self.array[i]
        
        return self.array
