# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        
        def tranverse(root, res):
            if root is None:
                return None
            
            tranverse(root.left, res)
            res.append(root.val)
            tranverse(root.right, res)
        
        records = []
        tranverse(root, records)

        records.append(val)

        def build(start, end):
            if start >= end:
                return
            
            idx = records.index(max(records[start:end]))
            node = TreeNode(records[idx])

            node.left = build(start, idx)
            node.right = build(idx+1, end)

            return node
        
        return build(0, len(records))