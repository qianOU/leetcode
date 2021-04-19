# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if root is None:
            return False
        
        q = collections.deque([root])
        flag = 0 # 控制奇偶数
        while q:
            sz = len(q)
            flag += 1 # 表示奇数
            begin_odd = float('-inf')
            begin_even = float('inf')
            for _ in range(sz):
                top = q.popleft()
                
                # 对奇数层进行校验
                if (top.val+flag)%2:
                    return False
                if flag % 2 and begin_odd >= top.val:
                    return False
                elif flag %2:
                    begin_odd = top.val

                # 对偶数层进行校验
                if flag % 2==0 and begin_even <= top.val:
                    return False
                elif flag %2==0:
                    begin_even = top.val
                
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
        
        return True