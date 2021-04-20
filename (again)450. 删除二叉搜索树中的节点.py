# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def dfs(root):
            if root is None:
                return
            
            if key < root.val:
                root.left = dfs(root.left)
            if key > root.val:
                root.right = dfs(root.right)
            
            if key == root.val:
                # 找寻左子树最大节点作为新的root替换点
                if root.left:
                    flag = 0 # 记录是否左子树中无右子树的存在
                    temp = root.left #记录 root 的前继节点
                    prev = root # 前继节点的父节点
                    while temp.right:
                        flag = 1 # 标志着左子树中有右子节点存在
                        prev = temp
                        temp = temp.right
                    root.val = temp.val # 更换值
                    if not flag: # 如果左子树中，无右子节点，则将root.left 设置为 temp.left
                        prev.left = temp.left
                        return root

                    # 如果左子树中，有右子节点，则将 前继节点的右子节点指向前继节点的左节点
                    prev.right = temp.left
                
                    return root
                else: # 如果没有左子树，直接用右子树来替换
                    return root.right
            
            return root

        return dfs(root)