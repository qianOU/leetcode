# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 回文序列的判读 可以通过
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        
        # 判断是否是符合的回文序列
        def isvalid(records):
            odd_kinds = sum(i%2 for i in records)
            return odd_kinds <= 1 # 只有奇数个数字总数小于等于 1 的时候，是回文序列

        self.ans = 0 # 记录总的合理路径数

        # 回溯
        def back_trace(root, records:list):
            if root is None:
                return 
        
            if root.left is None and root.right is None: # 到达叶子节点
                if isvalid(records):
                    self.ans += 1
            
            if root.left:
                records[root.left.val] += 1 # 做选择
                back_trace(root.left, records) 
                records[root.left.val] -= 1  # 撤回选择
            if root.right:
                records[root.right.val] += 1 # 做选择
                back_trace(root.right, records) 
                records[root.right.val] -= 1  # 撤回选择

        ans = list(range(10))
        ans[root.val] += 1
        back_trace(root, ans)
        return self.ans


    # 使用位运算
    """
    关键就在于用9个bit位表示节点的频次。
    9个bit位从后往前，依次表示1~9的频次的奇偶性，0表示偶数个，1表示奇数个，如此而已。 举个栗子：001 000 000，表示数字7出现了奇数次；001 000 100则表示，数字3和7都出现了奇数次。
    那么能成为伪回文的充要条件伪：9个bit位中1的个数 <= 1。
    如何表示 9 位比特位呢，
    比如对于
    """

    def pseudoPalindromicPaths (self, root: TreeNode) -> int:

        def dfs(root, records):
            pass
        pass
    
