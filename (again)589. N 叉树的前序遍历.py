"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # 迭代
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        output = []
        stack = [root]
        while stack:
            one = stack.pop() 
            output.append(one.val)
            stack.extend(one.children[::-1]) # 子孙节点倒序入栈,就相当于正序出栈
        
        return output

    # 递归
    def preorder(self, root):
        ans  = []
        def bt(root):
            if root is None:
                return 
            ans.append(root.val)
            for i in root.children:
                bt(i)
        
        bt(root)
        return ans
            

