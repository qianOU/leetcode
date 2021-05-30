class Solution:
    # 思路 1：是使用 内置排序韩式
    # 思路2 ：可以使用桶排序
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        abs_min = 100
        total = 0
        nums.sort()
        for i in nums:
            if i < 0 and k > 0:
                total += -i
                k -= 1
            else:
                total += i
            
            abs_min = min(abs(i), abs_min)
            
            
        if k%2:
            return total - 2*abs_min
        return total
        


