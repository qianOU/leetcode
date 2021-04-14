# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 
        
        stack = [root] # 前序遍历维持的隐含栈

        node = TreeNode(None) # 虚拟头节点， 指向根节点
        while stack:
            node.left = None
            node.right =  stack.pop()# 记录前一节点的右指针指向当前前序遍历得到的点
            node = node.right #  更新指针到当前节点
            if not node: # 如果遍历到最后一个元素，退出
                break
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                

            

        return root
           
            
