"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        ans = []
        def back_tranverse(root):
            if root is None:
                return 
            
            for i in range(len(root.children)):
                back_tranverse(root.children[i])
            
            ans.append(root.val)
        
        back_tranverse(root)
        return ans