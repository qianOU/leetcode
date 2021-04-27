class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        items = preorder.split(',')
        if not items:
            return False
        stack = [items[0]]
        i = 1
        n = len(items)
        while i < n:
            top = stack.pop()
            if items[i] != '#':
                stack.append(items[i])
            


        
