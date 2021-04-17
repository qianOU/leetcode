# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        import collections
        ans = []
        q = collections.deque([root])
        while q:
            sz = len(q)
            res = float('-inf')
            for _ in range(sz):
                top = q.popleft()
                if top.val > res:
                    res = top.val
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
        
            if res != float('-inf'):
                ans.append(res)
    
        return ans