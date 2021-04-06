"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root is None:
            return 0
        def depths(root, depth):
            """
            前序遍历
            """
            depth += 1  # 前序操作

            if not root.children: # 判别是否已经遍历到根节点
                return depth
            # 递归： 择优选择 所有子节点中最大深度 作为答案
            return max(depths(c, depth) for c in root.children)
    
        def depths2(root):
            """
            基于后序遍历
            """
            if not root.children:
                return 1 # 叶子节点设为 深度初始值 为 1
            
            return max(depths2(c) for c in root.children) + 1

        return depths(root, 0)