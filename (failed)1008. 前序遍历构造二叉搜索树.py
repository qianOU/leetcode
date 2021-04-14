# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 前序遍历还原树
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def back(nums, par):
            if not nums:
                return
            item = nums.pop(0)
            root = TreeNode(item)
            if item < par:
                