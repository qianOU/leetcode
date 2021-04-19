# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 解法一：BFS
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        true_val = lambda x: x if x is None else x.val 

        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        
        q1 = [root1]
        q2 = [root2]

        while q1 and q2:
            sz1 = len(q1)
            sz2 = len(q2)
            if sz1 != sz2:
                return False
            # print(sz1, sz2)
            for _ in range(sz1):
                node1 = q1.pop(0)
                node2 = q2.pop(0)
                
                if node1 is None and node2 is None:
                    continue

                if node1.val != node2.val:
                    return False

                if true_val(node1.left) == true_val(node2.left) and true_val(node1.right) == true_val(node2.right):
                    q1.extend([node1.left, node1.right])
                    q2.extend([node2.left, node2.right])
                    continue
                if true_val(node1.left) == true_val(node2.right) and true_val(node1.right) == true_val(node2.left):
                    q1.extend([node1.left, node1.right])
                    q2.extend([node2.right, node2.left])
                    continue
                else:
                    return False
            
        if q1 or q2:
            # print(q1, q2)
            return False

        return True

    # 解法二：递归 （优雅！！！）
    # 递归函数定义为比较 root1 和 root2 是否相等
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is root2: # 表明都是 None
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or \
            self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left) # 翻转时的比较结果