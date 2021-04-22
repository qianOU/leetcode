# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    #  字典 来保存每一个节点为根节点时的节点树信息， 太浪费内存
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        # 红色节点，将树分成三个部分，我们要比较三个部分中，节点数目大于树的节点总数目一半的部分是否存在

        root2 = root
        
        records = {None:0} #记录，以 key 为 root 的子树的节点总数

        ans = []
        def dfs(root):
            if root is None:
                return 0
            
            if root.val == x:
                ans.append(root.left.val if root.left else None)
                ans.append(root.right.val if root.right else None)

            item = dfs(root.left) + dfs(root.right) + 1
            records[root.val] = item
            return item
        
        
        dfs(root)

        return max(records[ans[0]], records[ans[1]], records[root.val]-records[ans[0]]-records[ans[1]]-1) > 1/2*records[root.val]

    # 使用全局变量，只保存目标节点左右子树的节点总数
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        
        # 后序遍历
        # 函数意义：返回以 root 为根节点的子树 规模大小，也就是节点总数
        self.right_nums = self.left_nums = 0
        def dfs(root):
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if root.val == x:
                self.right_nums = right
                self.left_nums = left
            
            return 1 + left + right
        
        total = dfs(root)

        return any(i > total/2 for i in 
        (self.right_nums, self.left_nums, total - self.right_nums - self.left_nums - 1))