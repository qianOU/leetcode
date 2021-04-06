# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # bfs
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        self.min = float('inf')
        self.lastone = float('-inf')
        def bt(root):
            if root is None:
                return
            # 中序遍历
            bt(root.left)
            if root.val - self.lastone < self.min:
                self.min = root.val - self.lastone
            self.lastone = root.val
            bt(root.right)

        bt(root)
        return self.min


        


# 由层次遍历，还原一棵二叉树
def back_tree(nums = [1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]):
    root =  TreeNode(nums.pop(0))
    queue = []
    queue.append(root)

    while len(queue) and len(nums):
       q = queue.pop(0)
       if q is None:
           continue
       q.left = TreeNode(nums.pop(0)) if nums[0] is not None else nums.pop(0)
       q.right = TreeNode(nums.pop(0)) if nums[0] is not None else nums.pop(0)
       queue.append(q.left)
       queue.append(q.right)


    return root


root = back_tree([90,69,None,49,89,None,52])

A = Solution().minDiffInBST(root)
print(A)
