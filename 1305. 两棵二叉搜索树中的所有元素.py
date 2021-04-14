# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def middle(s, record=[]):
            if s is None:
                return 
            middle(s.left, record)
            record.append(s.val)
            middle(s.right, record)
        
        record_1 = []
        record_2 = []
        middle(root1, record_1)
        middle(root2, record_2)

        # 使用内置sorted函数
        # return sorted([*record_1, *record_2])

        # 归并算法
        def merge(s, t):
            ans = []
            if not s or not t:
                return s or t
            l1 = 0
            l2 = 0
            len_1 = len(s)
            len_2 = len(t)
            while l1 < len_1 and l2 < len_2:
                if s[l1] < s[l2]:
                    ans.append(s[l1])
                    l1 += 1
                else:
                    ans.append(t[l2])
                    l2 += 1

            if l1 < len_1:
                ans.extend(s[l1:])
            elif l2 < len_2:
                ans.extend(t[l2:])
            return ans
        
        return merge(record_1, record_2)
