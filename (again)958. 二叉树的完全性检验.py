# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS 
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root is None:
            return False
        import collections
        q = collections.deque([root])

        while q:
            sz = len(q)
            for i in range(sz):
                top = q.popleft()
                if not top: # 如果遇见·空节点，则若是完全二叉树的话，剩下队列中所有的节点都会是空节点
                    return all(i is None for i in q)
                q.append(top.left)
                q.append(top.right)

        return True