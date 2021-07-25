# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 打家劫舍问题具有一个贪心的性质，就是尽可能的去取更多的点
class Solution:
    # 记忆化 递归
    def rob(self, root: TreeNode) -> int:
        
        memory = {}
        # 后序遍历问题
        # 递归函数定义为 抢劫 以 root 为根节点 的树 能获得的最大收益
        def dfs(root):
            if root is None:
                return 0

            if root in memory:
                return memory[root]
            
            # 拿取 根节点，则根节点的下一次不能被拿，转到 下下次决策
            one = root.val + (0 if root.left is None else dfs(root.left.left) + dfs(root.left.right)) + \
                (0 if root.right is None else dfs(root.right.left) + dfs(root.right.right))

            # 不拿更节点的时候，转到下一层决策
            two = dfs(root.left) + dfs(root.right)

            # 返回最大值
            memory[root] = max(one, two)

            return memory[root]
        
        return dfs(root)

    # 优化， 记忆化的字典空间
    def rob(self, root: TreeNode) -> int:
        # 返回在面对 root子树时，偷取 root 和 不偷取 root 的最大值
        def dfs(root):
            if root is None: return 0, 0
            
            lselect, lnot = dfs(root.left)
            rselect, rnot = dfs(root.right)

            return root.val + lnot + rnot, max(lselect, lnot) + max(rselect, rnot)
        
        return max(dfs(root))
            