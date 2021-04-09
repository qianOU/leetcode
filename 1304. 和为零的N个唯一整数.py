class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n%2 == 1:
            ans = [0]
        pairs = n//2
        new = list(range(1, pairs+1))
        return [*ans, *new, *[-i for i in new]]