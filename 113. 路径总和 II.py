# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def back_trace(root, res, cum): # res 记录走的路径
            if root is None:
                return []

            if not (root.left or root.right): #代表叶子节点时
                if cum == targetSum:
                    ans.append(res.copy())

            if root.left:
                res.append(root.left.val)
                back_trace(root.left, res, cum+root.left.val) # 下一级决策
                res.pop()

            if root.right:
                res.append(root.right.val)
                back_trace(root.right, res, cum+root.right.val)
                res.pop()

        dumy = TreeNode(None)
        dumy.left = root
        back_trace(dumy, [], 0) # res中初始化的0，表示根节点之前的累计和为0
        # print(root)
        return ans