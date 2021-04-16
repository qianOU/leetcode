# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        # 构造中序遍历 值和索引的映射关系
        self.v2i = {j:i for i,j in enumerate(inorder)}
        index = 0 # 记录遍历的前序节点位置

        # dfs，由中序遍历确定某一个节点的左右子树范围，由前序遍历得知 根节点
        def dfs(left, right):
            nonlocal index
            if index == len(preorder):
                return # 构造树完成
            if left > right:
                return # 该节点没有子树信息
            
            idx = self.v2i[preorder[index]]
            root = TreeNode(preorder[index])
            index += 1

            
            root.left = dfs(left, idx-1)
            root.right = dfs(idx+1, right)

            return root
        
        return dfs(0, len(inorder))
            

            
      