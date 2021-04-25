class Solution:
    def minOperations(self, logs: List[str]) -> int:
        import re
        layers = 0
        for i in logs:
            if i == '../':
                layers = layers - 1 if layers >= 1 else 0
            if re.search('^[^.]*?/', i):
                layers += 1
        
        return layers 