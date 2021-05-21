class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        s = list(s)
        n = len(s)

        visited = set([s])
        min_ = '9'*n
        def back_trace(cur, round):
            nonlocal min_
            min_ = min(min_, ''.join(cur))
            
            

            
