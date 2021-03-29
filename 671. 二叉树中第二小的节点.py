# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def bt(root):
            # print(root.val, root.left, root.right)
            if root is None:
                return 
            if root.left is None:
                return bt(root.right)
            if root.right is  None:
                return bt(root.left)
            minnode = min(root.left.val, root.right.val)
            if minnode!=root.val:
                res.append(minnode)
            elif root.left.val > minnode:
                res.append(root.left.val)
            elif root.right.val > minnode:
                res.append(root.right.val)
            if minnode==root.val:
               
                if root.left.val == minnode:
                    bt(root.left)
                if root.right.val == minnode:
                    bt(root.right)

        bt(root)
        print(res)
        return -1 if len(res) == 0 else min(res)


# 由层次遍历，还原一棵二叉树
def back_tree(nums = [1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]):
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

root = back_tree()
A = Solution().findSecondMinimumValue(root)
print(A)
