class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = [0]*3
        for i in bills:
            ten, five = divmod(i-5, 10)
            have_10 = min(ten, money[1])
            money[1] -= have_10
            have_5 = five // 5 + (ten-have_10)*2
            money[0] -= have_5
            if money[0] < 0:
                return False
            
            money[i%10] += 1
        
        return True