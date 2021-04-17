# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        import collections
        ans = []
        q = collections.deque([root])
        while q:
            sz = len(q)
            res = []
            for _ in range(sz):
                top = q.popleft()
                res.append(top.val)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
                
            ans.append(res)
        
        return ans