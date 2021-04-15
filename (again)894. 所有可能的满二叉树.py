# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归只需要明确递归函数的功能；着眼于当前结点，不要想子问题
    # 明确递归退出条件
    # 本函数的功能就是返回 又 n 个结点构成的满二叉树列表
    # 因为满二叉树的左子树和右子树都是满二叉树，所以存在递归结构
    # 并且只有n=奇数时，才可能是满二叉树

    # 备忘录，防止重复计算问题
    memo = {0:[], 1:[TreeNode(0)]}
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n not in self.memo:
            ans = []
            for i in range(1, n, 2):
                y = n - i - 1 # y 标记的是右子树的结点数了； i 标记的是左子树的结点数
                left_items = self.allPossibleFBT(i)
                right_items =  self.allPossibleFBT(y)
                for left in left_items:
                    for j in right_items:
                        node = TreeNode(0)
                        node.left = left
                        node.right = j
                        ans.append(node)
                
            self.__class__.memo[n] = ans
        return  self.__class__.memo[n]
        