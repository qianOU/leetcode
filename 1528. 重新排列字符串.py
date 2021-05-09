class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join(i for _,i in sorted(zip(indices, s)))