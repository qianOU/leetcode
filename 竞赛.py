class Solution:
    # BFS
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        from collections import deque
        
        q = deque()