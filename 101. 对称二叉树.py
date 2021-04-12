# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS + 栈判断每一层是否对称
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if  root is None:
            return True
        
        q = [root] # 存放节点队列
        stack = [root.val] # 初始化
        while q:
            sz = len(q)
            
            for i in range(sz):
                node = q.pop(0)
                if i < sz//2:
                    stack.append(node.val if node is not None else None)
                else:
                    # print(stack, node.val)
                    if stack[-1] == node == None or \
                    (stack[-1] is not None and node is not None and \
                        stack[-1] == node.val):
                        stack.pop()
                    else:
                        return False
                    
                if node is not None:
                    q.append(node.left)
                    q.append(node.right)
            
            stack = [] #查看是否匹配
        return True

    # 迭代方法，使用两个指针
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            
            return root1.val == root2.val and (
                helper(root1.left, root2.right) # 判断root1 指向的树的左节点是否与 root2指向的右节点相等
                and helper(root1.right, root2.left) # 判断root1 指向的树的右节点是否与 root2指向的左节点相等
            )
        
        if root is None:
            return True
        else:
            return helper(root.left, root.right) # 检查根节点的左右子树