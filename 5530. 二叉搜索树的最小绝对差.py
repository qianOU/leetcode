# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans = []
        q = [] # 队列
        q.append(root)
        while q:
            one = q.pop(0)
            if one is None:
                continue
            ans.append(one.val)
            q.append(one.left)
            q.append(one.right)
        
        aa = sorted(ans)
        for i in range(len(aa), 0, -1):
            aa[i] -= aa[i-1]
        return min(aa[1:])