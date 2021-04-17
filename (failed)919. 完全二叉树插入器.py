# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.ans = [root]
        self.index = 0

    def insert(self, v: int) -> int:
        self.ans.append(TreeNode(v))
        self.index += 1
        par = (self.index-1) // 2
        retur self.ans[self.index].val


    def get_root(self) -> TreeNode:
        return self.ans[0]
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()