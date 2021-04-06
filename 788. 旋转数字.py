class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        n = len(A)
        if len(A) != len(B): return False
        if n == 0: return True
        
        set_A = set()

        for i in range(n):
            set_A.add(A[i:n] + A[:i%n])
        return B  in set_A
