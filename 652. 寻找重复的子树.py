# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if root is None:
            return []

        import collections
        # 以树的中序遍历方式作为建
        records = set()
        have_same_tree = set()
        ans = [] 
        # 后序遍历
        def dfs(root):
            if root is None:
                return '#'
            
            
            
            left = dfs(root.left)
            right = dfs(root.right)

            # PS : 中序遍历是无法反序列化的，即 序列化后字符串与树结构不是一一对应的
            temp = left +',' + right  +','+ str(root.val) # 使用后序遍历的序列化方式 
            # print(temp)
            if temp not in records:
                records.add(temp)
            elif temp not in have_same_tree:
                have_same_tree.add(temp)
                ans.append(root)
            
            # if root.left is None and root.right is None:
            #     return str(root.val)
            return temp
        
        dfs(root)
        

        return ans
