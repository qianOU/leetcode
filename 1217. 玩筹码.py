class Solution:
    # 贪心 
    # 所有奇数 和所有偶数都是互通的
    # 最后奇数多或者偶数多的部分不移动，完全移动另外一部分，而且奇数和偶数只差 1
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = even = 0
        for i in position:
            if i%2: odd += 1
            else: even += 1
        
        return min(odd, even)

