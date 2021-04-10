class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        ans = [1]
        for i in range(2, int(num**.5)+1):
            if num %i==0:
                ans.append(i)
                ans.append(num/i)
        
        return sum(ans) == num