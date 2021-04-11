# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 分治思想
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        if len(nums)==1:
            return TreeNode(nums[0])
        # 找寻中点
        n = len(nums)
        mid = n//2
        # print(nums, mid)
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root