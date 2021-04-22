# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 写的过于复杂
    # 后序遍历
    def longestUnivaluePath(self, root: TreeNode) -> int:
        longest = 0
        # dfs 递归函数定义为： 返回 节点的值，以及以该节点为根节点能形成的 同值路径的list， 其中list第一个元素是root在同值路径上能形成的最长路径
        def dfs(root):
            nonlocal longest

            if root is None:
                return None, [0] 
            
            
            l_v, l_long = dfs(root.left)
            r_v, r_long = dfs(root.right)

            if l_v == r_v == root.val: # 如果 左节点 == 右节点 == 根节点
                if l_long[0] + r_long[0] + 2 > longest: # 判断是否是最长路径
                    longest = l_long[0] + r_long[0] + 2
                return root.val, [max(l_long[0], r_long[0])+1, l_long[0] + r_long[0] + 2,max(l_long[1:]), max(r_long[1:])]
            if l_v == root.val: # 只有左子节点==root时
                if l_long[0]+1 > longest:
                    longest = l_long[0] + 1
                return root.val, [l_long[0]+1, max(l_long[1:]), max(r_long)]
            if r_v == root.val: # 只有右子节点==root时
                if r_long[0]+1 > longest:
                    longest = r_long[0] + 1
                return root.val, [r_long[0]+1, max(r_long[1:]), max(l_long)]
            else: # 左右子树都没有相等的情况时
                return root.val, [0, max(l_long), max(r_long)]
        
        # dfs(root)

        # return longest
        """优雅的写法"""
        # 递归函数 定义 为 以 root 为 箭头起始的树 能为 其 父节点提供的最长路径长度
        # 注意这里 使用了箭头起点， 也就意味着 root 是在 同值路径之上的
        longest_arr = 0
        def arr_length(root):
            nonlocal longest_arr
            if not root: return 0

            left = arr_length(root.left)
            right = arr_length(root.right)

            cur_left_arr = cur_right_arr = 0

            if root.left and root.left.val == root.val:
                cur_left_arr = left + 1
            if root.right and root.right.val == root.val:
                cur_right_arr = right + 1
            
            longest_arr = max(longest_arr, cur_left_arr+cur_right_arr) # 比较确定最长同值路径长度

            return max(cur_left_arr, cur_right_arr) # 返回以root为起点的最长同值路径长度

        arr_length(root)

        return longest_arr            

        
