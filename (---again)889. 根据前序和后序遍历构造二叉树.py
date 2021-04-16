# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 同样的主要是为了找寻子问题
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:

        self.map = {i:j for j,i in enumerate(post)}
        def dfs(pre, post):
            if not pre: # 没有右子树的情况
                return 
            root = TreeNode(pre[0])
            if len(pre)==1: return root # 只有一个结点时

            L = post.index(pre[1]) + 1 # pre1 代表的是先序遍历的左节点
            root.left = dfs(pre[1:L+1], post[:L])
            root.right = dfs(pre[L+1:], post[L:-1])
            return root
        return dfs(pre, post) 