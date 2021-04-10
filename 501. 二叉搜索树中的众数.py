# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        my_dict = {}
        def bt(root):
            if root is None:return 

            my_dict[root.val] = my_dict.get(root.val, 0) + 1
            bt(root.left)
            bt(root.right)
        
        bt(root)
        # a = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
        # ans = []
        # for i in a:
        #     if i[1] == a[0][1]:
        #         ans.append(i[0])
        #     else:
        #         break
        max_n, res = 0, []
        for k, v in my_dict.items():
            if max_n < v:
                max_n = v
                res = [k]
            elif max_n == v:
                res.append(k)
        
        return res
            

        
        return ans