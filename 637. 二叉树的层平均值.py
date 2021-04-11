# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = [root]
        ans = []
        
        while q:
            sz = len(q)
            sum_ = 0
            for _ in range(sz):
                one = q.pop(0)
                sum_ += one.val
                if one.left is not None:
                    q.append(one.left)
                if one.right is not None:
                    q.append(one.right)
            
            ans.append(sum_/sz)
            sum_ = 0
        return ans