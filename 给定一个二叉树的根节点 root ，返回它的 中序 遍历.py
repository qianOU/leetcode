# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        stack = []
        # 把当前节点的完全左子树路径压入栈
        def order(root):
            while root is not None:
                stack.append(root)
                root = root.left
        
        order(root) # 将根节点的完全左子树路径部分压入栈
        ans = []
        while stack:
            top = stack.pop() # 栈顶元素即为 最左端元素 出栈
            order( top.right) # 将当前节点的右子树部分也入栈
            ans.append(top.val)
        
        return ans