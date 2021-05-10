class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        arr = sorted(costs)
        residual = coins
        count = 0
        for i in arr:
            if residual >= i:
                count += 1
                residual -= i
            else:
                break
            
        return count