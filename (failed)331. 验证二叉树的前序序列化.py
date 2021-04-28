class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        items = preorder.split(',')
        import queue
        queue
        if not items:
            return False
        
        def dfs(state):
            if not items and state == 1: # 右子树
                return False
            
            elif not items and state == 0: # 左子树
                return True

            item = items.pop(0)

            if item == '#':
                return True

            return dfs(0) and dfs(1)
        

        return dfs(None) and not items


        
