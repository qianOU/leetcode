# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归方法
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 is None and t2 is None: return True
        elif t1 is None or t2 is None: return False
        return (t1.val == t2.val and self.checkSubTree(t1.left, t2.left) and self.checkSubTree(t1.right, t2.right)) or(
            self.checkSubTree(t1.left, t2) 
        ) or self.checkSubTree(t1.right, t2)
    
    # 序列化 + KMP匹配方法
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        # 先序遍历
        def serialize(root， res):
            if root is None: 
                res.append('#')
                return
            res.append(str(root.val))
            serialize(root.left, res)
            serialize(root.right, res)
            return res
        
        s = ','.join(serialize(t1, []))
        patten = ','.join(serialize(t2, []))

        class KMP:
            def __init__(self, pattern):
                self.next = self.getnext(patten)
                self.patten = pattern
            
            def getnext(self, patten):
                n = len(patten)
                next = [-1]*n
                next[0] = -1
                i, j = 0, -1 # 双指针
                while i < n-1:
                    if j < 0 or patten[i] == patten[j]:
                        i += 1
                        j += 1
                        next[i] = j
                    else:
                        j = next[j]
                return next
            
            def search(self, s):
                m = len(s)
                n = len(self.patten)
                i, j = 0, 0
                while i < m and j < n:
                    if j < 0 or s[i] == self.patten[j]:
                        i += 1
                        j += 1
                    else:
                        j = self.next[j]
                
                return j == n
        
        return KMP(patten).search(s)



