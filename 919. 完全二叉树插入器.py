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
        item = TreeNode(v)
        self.ans.append(item)
        self.index += 1
        par = (self.index-1) // 2
        if par%2:
            self.ans[par].left = item
        else:
            self.ans[par].right = item
        return self.ans[par].val


    def get_root(self) -> TreeNode:
        return self.ans[0]
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()