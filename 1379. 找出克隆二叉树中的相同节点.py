# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # BFS
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is None:
            return
        q_1 = [original]
        q_2 = [cloned]
        while q_1:
            node_base = q_1.pop(0)
            node_copy = q_2.pop(0)
            if node_base == target:
                return node_copy
            if node_base.left is not None:
                q_1.append(node_base.left)
                q_2.append(node_copy.left)
            if node_base.right is not None:
                q_1.append(node_base.right)
                q_2.append(node_copy.right)
                
