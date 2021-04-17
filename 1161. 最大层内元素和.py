# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return

        ans = float('-inf')
        max_layer = 0

        import collections
        q = collections.deque([root])
        count_layer = 0
        sum_layer = 0
        while q:
            count_layer += 1
            sz = len(q)
            sum_layer = 0
            for _ in range(sz):
                node = q.popleft()
                sum_layer += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if sum_layer > ans:
                ans = sum_layer
                max_layer = count_layer
        
        return max_layer

            