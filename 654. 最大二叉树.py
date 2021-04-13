# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def constructor(nums):
            if not nums:
                return None
            
            max_val = max(nums)
            idx = nums.index(max_val)
            node  = TreeNode(max_val)
            node.left = constructor(nums[:idx])
            node.right = constructor(nums[idx+1:])
            return node
        
        return constructor(nums)