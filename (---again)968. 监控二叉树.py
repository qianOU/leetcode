# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0
        # 贪心：尽量将摄像头按装在父节点上，后序遍历
        # 返回状态：0---当前节点无覆盖 1----当前节点有摄像头 2----当前节点有覆盖
        def dfs(root):
            # 空节点表示的是有覆盖
            if root is None: return 2
            left = dfs(root.left)
            right = dfs(root.right)
            if left == 0 or right == 0: 
                self.ans += 1
                return 1 # 如果左右子节点都是无覆盖的话，当前节点需要有摄像头
            elif (left | right) & 1: return 2 # 如果左右子节点有其一有摄像头的话，当前节点表明是有覆盖的
            elif (left & right) & 2: return 0  # 如果左右子节点都是有覆盖的话，当前节点表明是无覆盖的

        # 如果头节点是无覆盖状态的时候
        if dfs(root) == 0: 
            print(self.ans)
            self.ans += 1

        return self.ans