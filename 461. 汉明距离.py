class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^y
        count = 0 
        while ans:
            ans, i = divmod(ans, 2)
            count += i
        
        return count

print(Solution().hammingDistance(1,4))