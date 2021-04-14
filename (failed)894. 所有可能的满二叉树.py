# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n < 1:
            return []
        root = TreeNode(0)
        import copy
        self.ans = []
        # 回溯
        def backtrace(root, count=0, res=[]):
            if count == n:
                self.ans.append(res.copy())
                return
            
            if count > n-2:
                return 
            node = TreeNode(0)
            root.left = node
            root.right = copy.deepcopy(node)
            res.append(root.left, root.right)
            backtrace(root.left, count+2, res + [root.left, None, None])
            backtrace(root.right, count+2, res + [None, None, root.right])
        
        res = [root]
        backtrace(root, 1, res)
        print(len(self.ans))
        return self.ans
