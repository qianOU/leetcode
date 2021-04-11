# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        q = [] # 存储路径节点
        q.append(root)
        ans = [str(root.val)] #存储每个节点的路径值
        sum_ = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                node = q.pop(0)
                v = ans.pop(0)
                # 判别是否已经到达根节点
                if node.left is None and node.right is None:
                    sum_ += int(v, base=2)
                if node.left is not None: 
                    q.append(node.left)
                    ans.append(v+str(node.left.val))
                if node.right is not None:
                    q.append(node.right)
                    ans.append(v+str(node.right.val))
        return sum_

    # 前序遍历 递归
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def helper(root, sum_):
            if root is None:
                return 0
            
            # 更节点操作
            sum_ = (sum_ << 1) + root.val # 位运算符优先级低于 数学运算符,所以必须加括号

            # 如果到达叶子节点,返回sum_
            if root.left is None and root.right is None:
                return sum_
            
            # 做子树的叶子节点 + 右子树的叶子节点
            return helper(root.left, sum_) + helper(root.right, sum_)
        
        return helper(root, 0)

