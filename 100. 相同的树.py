# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # DFS
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # base -case 叶子节点
        if (p is None and q is None):
            return True
        elif None in (p,q):
            return False
        
        # 根节点操作
        if p.val != q.val:
            return False
        
        return all( [
                self.isSameTree( p.left, q.left),
                self.isSameTree(p.right, q.right)
                    ]
            )

    # BFS 效率比DFS更高更高
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # base -case 叶子节点
        if (p is None and q is None):
            return True
        
        q1 = [] # BFS队列
        q2 = [] 

        q1.append(p)
        q2.append(q)
        while len(q1):
            sz = len(q1)
            for i in range(sz):
                p1 = q1.pop(0)
                p2 = q2.pop(0)
                if p1 is None and p2 is None:
                    continue
                elif None in (p1, p2) or p1.val != p2.val:
                    return False
                else:
                    q1.append(p1.left)
                    q1.append(p1.right)
                    q2.append(p2.left)
                    q2.append(p2.right)
                
            
        return  len(q2)==0


