"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        attrs = ['topLeft', 'topRight', 'bottomLeft', 'bottomRight']

        def dfs(root_a, root_b):
            if root_a is None and root_b is None: return
            node = Node(0, False, None, None, None, None)
            if root_a.isLeaf and root_b.isLeaf:
                node.val, node.isLeaf = root_a.val | root_b.val, True
                return node
            elif (root_a.isLeaf and root_a.val)  or (root_b.isLeaf and root_b.val):
                node.val, node.isLeaf = 1, True
                return node
            children = []
            for child in attrs:
                children.append(dfs(
                    getattr(root_a, child) if getattr(root_a, child) else root_a,
                    getattr(root_b, child) if getattr(root_b, child) else root_b
                    )
                    )
            if all(i.val == children[0].val and i.isLeaf for i in children):
                node.val, node.isLeaf = children[0].val, True
                return node

            for i in range(4):
                setattr(
                    node, attrs[i], children[i]
                    )
            return node

        return dfs(quadTree1, quadTree2)   
                