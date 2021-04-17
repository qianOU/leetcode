# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # 自底向上 后序遍历
        # 返回 以 root 为根节点的树的深度, 和符合条件的根节点 （树的深度从叶子节点开始计算，叶子节点记为深度1, ）
        # 依此推 叶子节点的父亲节点 记为 深度 2，....
        def dfs(root):
            if root is None:
                return 0, None
            
            left, l_node = dfs(root.left)
            right, r_node = dfs(root.right)

            # 已经遍历，root节点，其是左右子树最深深度 + 1
            if left == right:
                return left+1, root 
            elif left > right:
                return left+1, l_node
            else:
                return right+1, r_node
        
        return dfs(root)[1]
