# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        if root is None:
            return 0
       
        res = [] # 保存后序遍历的结果
        def dfs(root):
            
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            root.val = left + right  + root.val
            res.append(root.val)
            return root.val
        
        def binsearch(ans, target, flag=1):
            # flag 控制搜索的 索引 类型
            left = 0
            right = len(ans)-1
            while left <= right:
                mid = left + (right - left) //2
                if flag:  # 找寻 >= target  的第一个值
                    if ans[mid] >= target:
                        right = mid - 1
                    else:
                        left = mid + 1
                else: # 找寻 <= target 的第一个元素
                    if ans[mid] <= target:
                        left = mid + 1
                    else:
                        right = mid - 1
            if flag:    
                return left
            else:
                return right
        
        dfs(root)
        res = sorted(res # 使用二分第一步进行 排序
        a1 = binsearch(res, root.val/2, 1) # 找寻 大于 等于 N/2 的第一个元素
        a2 = binsearch(res, root.val/2, 0) # 找寻 小于 等于 N/2 的第一个元素
        item = max(res[a1]*(root.val - res[a1]),
         res[a2]*(root.val - res[a2]) )% ( 10**9 + 7)
        # print(res[a1], res[a2], a1, a2, root.val)
        return item 



        
        