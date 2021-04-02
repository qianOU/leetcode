# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 通用框架
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def backtrack(root, p, q):
            # base-case
            if root is None:
                return 
            if root.val in (p.val, q.val):
                return root


            left = backtrack(root.left, p, q)


            right = backtrack(root.right, p, q)

            if left is None and right is None:
                return None
            elif left is not None  and right is not None:
                return root
            else:
                return left if right is None else right
            
        return backtrack(root, p, q)

        # 使用 二叉搜索树特性进行剪枝
        # 并且 题目 已知 节点一定存在 二叉树中
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root # 因为题目假定 p 和 q 是存在在树中的

# 由层次遍历，还原一棵二叉树
def back_tree(nums = [6,2,8,0,4,7,9,None,None,3,5]):
    root =  TreeNode(nums.pop(0))
    queue = []
    queue.append(root)

    while len(queue) and len(nums):
       q = queue.pop(0)
       q.left = TreeNode(nums.pop(0))
       q.right = TreeNode(nums.pop(0))
       queue.append(q.left)
       queue.append(q.right)

    return root

root = back_tree( [6,2,8,0,4,7,9,None,None,3,5])

A = Solution()
print(A.lowestCommonAncestor(root, TreeNode(0), TreeNode(4)).val)

